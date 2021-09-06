#!/usr/bin/env python

import re
import time

from section import Section

class Table(object):
    """
    A table contains several @class Section

    - Horizontal view

        section-1
        ---------
        section-2
        ---------
        section-3
    """
    def __init__(self, name="", ftr="", width=800, height=600, sep="-"):
        self.name = name
        self.ftr = ftr
        self.width = width          # max width
        self.height = height        # max height
        self.sep = sep
        self.sections = {}          # @dict {name: @class Section}
        self.hori = True

    def __str__(self):
        div = "%s\n" % (self.sep * self.size()[0])
        return div.join(map(lambda x: str(x),
                            sorted(self.sections.itervalues(),
                                   key=lambda y: y.id)) + [self.get_ftr()])

    def __repr__(self):
        return "Table(name=%r, sections=%r, hori=%r)"\
            % (self.name, self.sections, self.hori)

    def size(self):
        """Return the viewable size of the Table as @tuple (x,y)"""
        width = max(
            map(lambda x: x.size()[0], self.sections.itervalues()))

        height = sum(
            map(lambda x: x.size()[1], self.sections.itervalues()))

        return width, height

    def set_ftr(self, ftr):
        """
        Set footer for this table
        Accept the following regexps:

        %time : current time printed as "hh:mm:ss"
        """
        self.ftr = ftr

    def get_ftr(self):
        """
        Process footer and return the processed string
        """
        if not self.ftr:
            return self.ftr

        width = self.size()[0]
        return re.sub(
            "%time", "%s\n" % time.strftime("%H:%M:%S"), self.ftr).rjust(width)

    def get_section(self, name):
        if name in self.sections.iterkeys():
            return self.sections[name]
        return None

    def add_section(self, section):
        if isinstance(section, Section):
            self.sections[section.name] = section