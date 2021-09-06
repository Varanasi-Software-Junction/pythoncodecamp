#!/usr/bin/env python

import logging
from blessings import Terminal
from table import Table

class BlessingPainter(object):
    """
    A sample painter based on blessings package

    http://pypi.python.org/pypi/blessings
    """
    def __init__(self):
        self.term = Terminal()
        super(BlessingPainter, self).__init__()

    def enter_fullscreen(self):
        """
        Invoke before printing out anything.
        This method should be replaced by or merged to blessings package
        """
        self.term.stream.write(self.term.enter_fullscreen)
        self.term.stream.write(self.term.hide_cursor)

    def exit_fullscreen(self):
        """
        Invoke before printing out anything.
        This method should be replaced by or merged to blessings package
        """
        self.term.stream.write(self.term.exit_fullscreen)
        self.term.stream.write(self.term.normal_cursor)

    def paint(self, tbl):
        """
        Paint the table on terminal
        Currently only print out basic string format
        """
        if not isinstance(tbl, Table):
            logging.error("unable to paint table: invalid object")
            return False

        self.term.stream.write(self.term.clear)

        self.term.stream.write(str(tbl))
        return True