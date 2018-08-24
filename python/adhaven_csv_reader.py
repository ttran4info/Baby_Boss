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
import csv
# Set up the logger
LOGGER = logging.getLogger('adhaven_logs')

class adhaven_csv_reader(object):
   
    def __init__(self):
        """ adhaven_helper constructor """
        self.start_time = ""
        self.end_time = ""
        
    def print_csv_contents(self, filename):
        LOGGER.debug("Opening file: " + filename)
        status = False
        try:
            with open(filename, 'rb') as csvfile:
                myreader = csv.reader(csvfile, delimiter=',')
                for row in myreader:
                    print '|'.join(row)
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
            status = True
        return status 
        
   