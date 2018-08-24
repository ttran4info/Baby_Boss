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
from decimal import Decimal
from datetime import datetime
from datetime import timedelta
import urllib2
import urllib

# Set up the logger
LOGGER = logging.getLogger('adhaven_helper_logs')

class adhaven_helper(object):
   
    def __init__(self):
        """ adhaven_helper constructor """
        self.start_time = ""
        self.end_time = ""
        
    def split_string(self, my_string, delimiter):
        LOGGER.debug("string to split:" + my_string)
        LOGGER.debug("delimiter:" + delimiter)
        try:
            split_list = my_string.split(delimiter)
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
        return split_list
        
    def find_item_in_list(self, item, my_list=[]):
        status = False
        try:
            """Return first item in sequence where == True."""
            for x in my_list:
                if x == item: 
                    status = True
                    LOGGER.debug("Found Item: " + x)
                    break
                else:
                    LOGGER.debug("List Item: [" + x  + "] does not match [" + item + "]")
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
            status = True
        return status 
        
    def get_total_line_count(self, file_name):
        LOGGER.debug("file:" + file_name)
        try:
            cpn_file = open(file_name)
            count_lines = sum(1 for line in cpn_file)
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
        LOGGER.debug("file:" + file_name  + " line_count:" + str(count_lines))
        return count_lines
    
    def read_line_from_file(self, file_name, line_no):
        LOGGER.debug("file:" + file_name)
        line_no = int(line_no)
        try:
            f = open(file_name)
            lines=f.readlines()
            found_line = lines[line_no]
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
        return found_line

    def decode_url(self, original_url):
        LOGGER.debug("Original URL:" + original_url)
        try:
            decoded = original_url.replace("&amp;", "&")
        except OSError, error_msg:
            LOGGER.fatal(str(error_msg))
        return decoded
    
    def files_match(self, file_one, file_two):
        """ Determine if the two files match 
            Prerequisite:
                none
            Returns:
                True if the files match
                False if the files don't match
        """        
        LOGGER.debug('File1:' + file_one)
        LOGGER.debug('File2:' + file_two)
        try:
            if filecmp.cmp(file_one, file_two, False):
                return_status = True
            else:
                return_status = False
        except OSError, error_msg:
            LOGGER.fatal("Failed. Files not identical: " 
                         + file_one + " and: " + file_two )
            LOGGER.fatal(error_msg)
            return_status = False
           
        return return_status 
        
 
    # XXX000 This should be in a utilities class

    def extract_matching_regex(self, original_string, pattern):
        """ Determine if the string pattern occurs in the string
            Prerequisite:
                none
            Returns:
                True if the strings are a regex match
                False if the strings don't match
        """        
        LOGGER.debug(original_string)
        LOGGER.debug(pattern)
        text_found = ''
        try:
           found = re.search(pattern, original_string)
           if found:
               text_found = found.group(1)
           else:
               text_found = 'NONE_FOUND'
        except OSError, error_msg:
            LOGGER.fatal(error_msg)
        return text_found
    
    def regex_string_match(self, string_pattern, string_to_match):
        """ Determine if the string pattern occurs in the string
            Prerequisite:
                none
            Returns:
                True if the strings are a regex match
                False if the strings don't match
        """        
        LOGGER.debug(string_pattern)
        LOGGER.debug(string_to_match)
        try:
            if  re.search(string_pattern, string_to_match ):
                LOGGER.debug("found match")
                return_status = True
            else:
                LOGGER.debug("no match")
                return_status = False
        except OSError, error_msg:
            LOGGER.fatal("Failed. Strings are not a regex match.: " 
                         + string_pattern + " and: " + string_to_match )
            LOGGER.fatal(error_msg)
            return_status = False
           
        return return_status 
        
 
    # XXX000 This should be in a utilities class
    
    def regex_lines_match(self, file_name, string_pattern, 
                          skip_header_lines = 0):
        """ Determine if the lines in the file match the string pattern.
            Prerequisite:
                none
            Returns:
                True if the lines are a regex match
                False if the lines don't match
        """        
        LOGGER.debug(string_pattern)
        LOGGER.debug(file_name)
        LOGGER.debug(skip_header_lines)
        
        try:
            skip_header_lines = int (skip_header_lines)
        except:
            LOGGER.debug("skip_header_lines not int.")
            skip_header_lines =  0
          
        
        return_status = True
        try:
            regex = re.compile(string_pattern)
            lines = open(file_name).readlines()
            LOGGER.debug(lines)
            del lines[0 : int(skip_header_lines)]
            LOGGER.debug(lines)
            for line in lines:
                line = line.rstrip('\n')
                if not regex.search(line) :
                    LOGGER.debug("no match")
                    LOGGER.debug("Line: " + line)
                    return_status = False
                    break
        except OSError, error_msg:
            LOGGER.fatal("Failed. Strings in " + file_name 
                         + " are not a regex match to: " 
                         + string_pattern )
            LOGGER.fatal(error_msg)
            return_status = False
           
        return return_status 

    def get_timestamp(self):
        try:
            timestamp = datetime.now()
            formatted_timestamp = timestamp.strftime('%Y_%m_%d_%H:%M:%S')
            LOGGER.debug("Day Count: " + str(formatted_timestamp))
        except OSError, error_msg:
            LOGGER.debug("Error in calculating number of days: " + error_msg )
        return str(formatted_timestamp)

    def get_days_count(self, start_date, end_date):
        """ Calculate the number of days given the start and end date.
            This information is used to validate report data given a date range.
            Prerequisite:  Date format need to be given in the format %m/%d/%Y"
            Returns:
                The number of days between the start and end date. 
                For Example:  08/01/2012 - 08/05/2012  should return count of 5
            Example:   get_days_count('08/01/2012','08/05/2012')
        """        
        LOGGER.debug("Start: " + start_date)
        LOGGER.debug("End: " + end_date)
        try:
            date_format = "%m/%d/%Y"
            a = datetime.strptime(start_date, date_format)
            b = datetime.strptime(end_date, date_format)
            delta = b - a
            day_count = delta.days + 1
            LOGGER.debug("Day Count: " + str(day_count))
        except OSError, error_msg:
            LOGGER.debug("Error in calculating number of days: " + error_msg )
        return str(day_count)
 
    def format_string_thousands(self, string_to_format):
        LOGGER.debug("String to format: " + str(string_to_format))
        locale.setlocale(locale.LC_ALL, '')
        try:
            dec_value = Decimal(string_to_format)
            formated_string = locale.format("%d", dec_value , grouping=True)
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    
        return formated_string
 
    def split_household_data_into_list(self, string_to_split):
        LOGGER.debug("String to format: " + str(string_to_split))
        try:
            split_list = string_to_split.splitlines( )
            LOGGER.debug("length: " + str(len(split_list)))
            split_list.sort()
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    
        return split_list

    def get_default_start_date(self):
        LOGGER.debug("Getting Default Start Date...")
        date_string = ""
        try:
            today = datetime.now()
            #date_string = today.strftime("%m/%d/%Y")
            date_string = "%d/%d/%d"%(today.month, today.day, today.year)
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    
        return date_string
    
    def get_default_end_date(self):
        LOGGER.debug("Getting Default End Date...Current Time plus 1day...")
        date_string = ""
        try:
            today = datetime.now()
            today +=  timedelta(days=1)
            #date_string = today.strftime("%-m/%-d/%Y")
            date_string = "%d/%d/%d"%(today.month, today.day, today.year)
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    
        return date_string

    def smb_end_date_from_duration(self,datestring,duration):
        LOGGER.debug("Getting Default End Date...with Duration...")
        LOGGER.debug("date_string:" + datestring)
        LOGGER.debug("duration:" + duration)
        
        current_utc_time = datetime.utcnow().strftime("%Y-%m-%d")
        LOGGER.debug("Current UTC Time:" + current_utc_time)
        
        if current_utc_time == datestring:
                new_duration = int(duration)
        else:
                new_duration = int(duration) - 1
        
        LOGGER.debug("new duration:" + str(new_duration))
        date_string = ""
        try:
            today2 = datetime.strptime(datestring, "%Y-%m-%d")
            today = datetime.date(today2)
            today +=  timedelta(days=int(new_duration))
            #date_string = today.strftime("%-m/%-d/%Y")
            #date_string = "%d/%d/%d"%(today.month, today.day, today.year)
            date_string = "%04d-%02d-%02d"%(today.year, today.month, today.day)
            LOGGER.debug("date_string:" + date_string)
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    
        return date_string    
           
    def smb_restart_date(self,datestring,duration):
        LOGGER.debug("date_string:" + datestring)
        LOGGER.debug("duration:" + duration)
        current_utc_time = datetime.utcnow().strftime("%Y-%m-%d")
        LOGGER.debug("Current UTC Time:" + current_utc_time)
        new_duration = int(duration)
        date_string = ""
        try:
            today2 = datetime.strptime(datestring, "%Y-%m-%d")
            today = datetime.date(today2)
            today +=  timedelta(days=int(new_duration))
            date_string = "%04d-%02d-%02d"%(today.year, today.month, today.day)
            LOGGER.debug("date_string:" + date_string)
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    
        return date_string       
           
    def download_file_from_url(self,filename,url):
        """Download a file from a url to local directory"""
        LOGGER.debug("Filename:" + filename)
        LOGGER.debug("URL:" + url)
        try:
            #file_name = url.split('/')[-1]
            file_name = filename
            u = urllib2.urlopen(url)
            f = open(file_name, 'wb')
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            print "Downloading: %s Bytes: %s" % (file_name, file_size)
            
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                status = status + chr(8)*(len(status)+1)
                print status,
            f.close()
        except OSError, error_msg:
            LOGGER.debug("Error: " + error_msg )    

    def get_execution_time(self):
        """ Return the total execution time of operation.
        """
        return self.get_end_time() - self.get_start_time()
        
    def get_start_time(self):
        """ Return the start time of operation.
        """
        return self.start_time
        
    def set_start_time(self):
        """ Set the start time of operation.
        """
        self.start_time = time.time()
        return 
        
    def get_end_time(self):
        """ Return the end time of operation.
        """
        return self.end_time
        
    def set_end_time(self):
        """ Set the end time of operation.
        """
        self.end_time = time.time()
        return 

