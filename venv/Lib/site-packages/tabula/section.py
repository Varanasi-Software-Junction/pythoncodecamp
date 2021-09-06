#!/usr/bin/env python

import logging
import os
import ast

import numpy as np

UNITS_SUFFIX = ["", "K", "M", "G", "T"]
TYPE_META = "S512"

def conv_units(val, meta):
    """
    Format and convert units to be more human readable

    @return new val with converted units
    """
    if not val or not meta:
        return val

    try:
        val = float(val)
    except ValueError:
        logging.error("unable to apply convert units for %s" % val)
        return val

    suf = 0
    while val > 1024 and suf < 4:
        val /= 1024
        suf += 1

    return "%.2f%s" % (val, UNITS_SUFFIX[suf])

"""CONV_FUNCS: convert data before column alignments"""
CONV_FUNCS = {"units": conv_units}

"""DECO_FUNCS: decorate data after column alignments"""
DECO_FUNCS = {}

class Section(object):
    """
    A section appears on @class Table

    e.g:

    - Flat section:
        key1: val1, key2: val2
        key3: val3 ...

    - Grid section:
        Like a spreedsheet, with col and row headers

        name |  col1 |  col2
        row1 |  val1 |  val2
        row2 |  val3 |  val4

    """
    def __init__(self, name, id=0, width=800, height=600, sep="  ",
                 show_row_hdrs=True, show_col_hdrs=True,
                 show_col_hdr_in_cell=False, auto_resize=True,
                 conv_funcs=CONV_FUNCS, deco_funcs=DECO_FUNCS):
        """
        @param id: id/position to place a section on the table
        @param width : max width, use terminal width auto_resize is on
        @param height: max height

        @param show_row_hdrs : show row headers
        @param show_col_hdrs : show column headers
        @param show_col_hdr_in_cell : embed column header in each cell
        @param auto_resize : auto resize according to the size of terminal
        @param conv_funcs : func to convert data before column alignments
        @param deco_funcs : func to decorate data after column alignments
        """
        self.name = name
        self.id = id
        self.width = width
        self.height = height
        self.sep = sep
        self.show_row_hdrs = show_row_hdrs
        self.show_col_hdrs = show_col_hdrs
        self.show_col_hdr_in_cell = show_col_hdr_in_cell
        self.auto_resize = auto_resize
        self.conv_funcs = conv_funcs
        self.deco_funcs = deco_funcs
        self.arr = None
        self.meta = None
        self.irt = {}           # inverted-row-table @dict {row_name: row_num}
        self._create()

    def __repr__(self):
        return "Section(name=%r, width=%r, height=%r, sep=%r, "\
               "show_row_hdrs=%r, show_col_hdrs=%r, "\
               "show_col_hdr_in_cell=%r, arr=%r, irt=%r)"\
               % (self.name, self.width, self.height, self.sep,
                  self.show_row_hdrs, self.show_col_hdrs,
                  self.show_col_hdr_in_cell, self.arr, self.irt)

    def __str__(self):
        return self._format()[0]

    def _term_size(self):
        """
        Retrieve the size of the terminal

        @return [width, height]
        """
        return list(reversed(os.popen('stty size', 'r').read().split()))

    def align(self, arr):
        """
        Align columns, including column headers
        """
        if arr is None:
            return arr

        c_hdrs = self._get_col_hdrs()

        if self.show_col_hdr_in_cell:
            for hdr in c_hdrs:
                arr[hdr] = map(lambda col: ":".join([hdr, str(col)]), arr[hdr])

        if self.show_col_hdrs:
            widths = [max(len(str(col))
                      for col in arr[hdr].tolist() + [hdr]) for hdr in c_hdrs]
        else:
            widths = [max(len(str(col))
                      for col in arr[hdr].tolist()) for hdr in c_hdrs]

        # align column headers
        c_hdrs = map(lambda (c_hdr, width): c_hdr.ljust(width),
                     zip(c_hdrs, widths))

        # align data
        for n_row in range(len(arr)):
            arr[n_row] = tuple(map(lambda (col, width): col.ljust(width),
                                   zip(arr[n_row], widths)))

        return arr, c_hdrs, widths

    def _format(self):

        if self.arr is None:
            return "", 0, 0

        if self.auto_resize:
            self.width = int(self._term_size()[0])

        arr = self.apply_meta(self.arr, self.conv_funcs)
        arr = self.sort(arr)

        if arr is None:
            return ""

        arr, c_hdrs, widths = self.align(arr)
        arr = self.apply_meta(arr, self.deco_funcs)

        data = arr.tolist()
        height = len(data)

        if self.show_row_hdrs:
            height += 1
            if self.show_col_hdrs:
                string = self.sep.join(c_hdrs) + "\n"
            else:
                string = ""
            string += "\n".join(self.sep.join(col for col in row)
                                for row in data)
        else:
            widths = widths[1:]
            if self.show_col_hdrs:
                string = self.sep.join(c_hdrs[1:]) + "\n"
            else:
                string = ""
            string += "\n".join(self.sep.join(col for col in row[1:])
                                for row in data)

        return self.wrap(string, self.width),\
               min(self.width, sum(widths) + (len(widths) - 1) * len(self.sep)),\
               height

    def format(self):
        """
        Format the section to a presentable string

        See @func config() for how to override configurations

        @return (formatted string, viewable width, viewable height)
        """
        return self._format()

    def wrap(self, string, width):
        """
        Wrap lines according to width
        Place '\n' whenever necessary
        """
        if not string or width <= 0:
            logging.error("invalid string: %s or width: %s" % (string, width))
            return False

        tmp = ""
        for line in string.splitlines():
            if len(line) <= width:
                tmp += line + "\n"
                continue

            cur = 0
            length = len(line)
            while cur + width < length:
                cur = line[:cur+width].rfind(self.sep) + len(self.sep) - 1
                line = line[:cur] + "\n" + line[cur+1:]

            tmp += line + "\n\n"

        return tmp

    def apply_meta(self, arr, funcs):
        """
        Apply metadata to help formatting the output:

        - conv_funcs: convert data before column alignments
        - deco_funcs: decorate data after column alignments
        """
        if arr is None:
            logging.error("unable to convert data: emtpy section")
            return None

        tmp = np.copy(arr)
        for col in arr.dtype.names:
            for row in self._get_row_hdrs():
                meta = self._get_meta(row, col)
                for mk, mv in sorted(meta.iteritems()):
                    if mk in funcs.iterkeys():
                        tmp[col][self.irt[row]] = \
                            funcs[mk](tmp[col][self.irt[row]], mv)
        return tmp

    def config(self, show_row_hdrs=True, show_col_hdrs=True,
                show_col_hdr_in_cell=False, auto_resize=True):
        """
        Override the in-class params:

        @param show_row_hdrs : show row headers
        @param show_col_hdrs : show column headers
        @param show_col_hdr_in_cell : embed column header in each cell
        @param auto_resize : auto resize according to the size of terminal
        """
        self.show_row_hdrs = show_row_hdrs
        self.show_col_hdrs = show_col_hdrs
        self.show_col_hdr_in_cell = show_col_hdr_in_cell

    def size(self):
        """
        Return the viewable size of the section as @tuple (width, height)
        """
        return self._format()[1:]

    def sort(self, arr, col=None):
        if arr is None:
            logging.error("unable to sort empty section")
            return None

        if not col or col not in self._get_col_hdrs():
            return np.sort(arr, order=self._get_col_hdrs()[1:])
        else:
            return np.sort(arr, order=col)

    def add_cell(self, row="unknown", col="unknown",
                 val="unknown", type="int32", meta=""):
        """
        Add/update a val on cell [row, col]

        Create new rows or columns accordingly

        @param row : row header name
        @param col : column header name
        @param meta: meta data to control data display
        """
        if self.arr is None:
            self.arr = np.array(
                [(row, val)], dtype=[ (self.name, "S50"), (col, type)])
            self.meta = np.array(
                [(row, val)], dtype=[ (self.name, TYPE_META), (col, type)])
            self.irt[row] = 0

        if not row in self._get_row_hdrs():
            self._expand_row(row)

        if not col in self._get_col_hdrs():
            self._expand_col(col, type)

        try:
            self._add_cell(val, row, col, meta)
        except ValueError:
            logging.error("unable to add val %s to [%s,%s]: "
                          "not a compatible data type" % (val, row, col))
            return False

        return True

    def get_cell(self, row, col):
        #TODO
        raise NotImplementedError

    def add_row(self, name, vals):
        #TODO
        raise NotImplementedError

    def del_row(self, name):

        if self.arr is None:
            logging.error("unable to delete row %s: empty section" % name)
            return False

        if not name in self._get_row_hdrs() or\
           not name in self.irt:
            logging.error("unable to delete row %s: row doesn't exist" % name)
            return False

        row_num = self.irt[name]
        self.arr = np.delete(self.arr, row_num)
        self.meta = np.delete(self.meta, row_num)
        for k,v in self.irt.iteritems():
            if v > row_num:
                self.irt[k] = v - 1

        return True

    def _create(self):

        if not self.arr is None:
            logging.error(
                "unable to create table %s: already exist" % self.name)
            return False

        self.arr = np.array([], dtype=[(self.name, "S50")])
        self.meta = np.array([], dtype=[(self.name, TYPE_META)])

        return True

    def _get_meta(self, row, col):
        """
        Get metadata for a particular cell
        """
        if self.meta is None:
            logging.error("unable to get meta: empty section")
            return {}

        if not row in self._get_row_hdrs() or\
            not col in self._get_col_hdrs():
            logging.error("unable to get meta: cell [%s,%s] does not exist"
                          % (row, col))
            return {}

        meta_str = self.meta[col][self.irt[row]]
        try:
            meta = ast.literal_eval(meta_str)
            if isinstance(meta, dict):
                return meta
        except (SyntaxError, ValueError), e:
            logging.error("unable to parse meta string - %s: %s"
                          % (meta_str, e))

        return {}

    def _get_col_hdrs(self):

        if self.arr is None:
            logging.error("unable to get row headers: empty section")
            return ()

        return self.arr.dtype.names

    def _get_row_hdrs(self):

        if self.arr is None:
            logging.error("unable to get row headers: empty section")
            return ()

        return self.arr[self.name]

    def _expand_col(self, name, type="int32"):

        if self.arr is None:
            logging.error("unable to add column %s: empty section" % name)
            return False

        if name in self._get_col_hdrs():
            logging.error("unable to add column %s: already exist" % name)
            return False

        arr_dtype = self.arr.dtype.descr + [(name, type)]
        new_arr = np.zeros(self.arr.shape, dtype=arr_dtype)
        meta_dtype = self.meta.dtype.descr + [(name, TYPE_META)]
        new_meta = np.zeros(self.meta.shape, dtype=meta_dtype)

        for field in self.arr.dtype.fields:
            new_arr[field] = self.arr[field]
        for field in self.meta.dtype.fields:
            new_meta[field] = self.meta[field]

        self.arr = new_arr
        self.meta = new_meta
        return True

    def _expand_row(self, name):

        if self.arr is None:
            logging.error("unable to add row %s: empty section" % name)
            return False

        if name in self._get_row_hdrs():
            logging.error("unable to add row %s: already exist" % name)
            return False

        n_rows = len(self.arr)
        self.arr = np.insert(self.arr, n_rows, np.array([name,]), 0)
        self.meta = np.insert(self.meta, n_rows, np.array([name,]), 0)

        self.irt[name] = n_rows

        return True

    def _add_cell(self, val, row, col, meta=""):
        """
        @except ValueError : data type not compatible
        """
        if self.arr is None:
            logging.error("unable to add value %s to [%s,%s]: empty section"
                          % (val, row, col))
            return False

        if not row in self._get_row_hdrs() or\
                not row in self.irt:
            logging.error("unable to add value %s to [%s,%s]: row doesn't exist"
                          % (val, row, col))
            return False

        if not col in self._get_col_hdrs():
            logging.error(
                "unable to add value %s to [%s,%s]: column doesn't exist"
                % (val, row, col))
            return False

        self.arr[self.irt[row]][col] = val
        self.meta[self.irt[row]][col] = str(meta)

        return True