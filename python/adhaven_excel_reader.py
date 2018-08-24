"""
Copyright 2012 4Info 
Helper Python functions for ADHaven UI
"""
import locale
import logging
import time
import filecmp
import re
import os
import sys
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
# Set up the logger
LOGGER = logging.getLogger('adhaven_logs')

class adhaven_excel_reader(object):
   
    def __init__(self):
        """ adhaven_helper constructor """
        self.start_time = ""
        self.end_time = ""
        
    def print_workboook_contents(self, filename):
        LOGGER.debug("Opening file: " + filename)
        status = False
        try:
            from xlrd import open_workbook,cellname
            book = open_workbook(filename)
            sheet = book.sheet_by_index(0)
            LOGGER.debug("Sheet name: " + sheet.name)
            LOGGER.debug("Total Columns: " + str(sheet.ncols))
            LOGGER.debug("Total Rows: " + str(sheet.nrows))
            for row_index in range(sheet.nrows):
                for col_index in range(sheet.ncols):
                    print cellname(row_index,col_index),'-',
                    print sheet.cell(row_index,col_index).value
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
            status = True
        return status 
        
   