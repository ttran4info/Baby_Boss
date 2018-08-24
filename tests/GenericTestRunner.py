"""
Copyright 2012 4Info 
Generic Robot Framework Test Runner
"""

import  subprocess
import  os
import logging
# get info about this module
PATH = os.getcwd()
THIS_MODULE_NAME = os.path.splitext(__file__)[0]
print("Starting: " + THIS_MODULE_NAME)
# Set up the logger
LOGGER = logging.getLogger('RF_4Info_logs')
HDLR = logging.FileHandler(THIS_MODULE_NAME + '.log')
FORMATTER = logging.Formatter('%(asctime)s ' + 
                              '%(levelname)s ' + 
                              '%(module)s ' + 
                              '%(funcName)s ' + 
                              '%(lineno)d ' + 
                              '%(message)s ')
HDLR.setFormatter(FORMATTER)
LOGGER.addHandler(HDLR) 
LOGGER.setLevel(logging.DEBUG) 

LOGGER.info("MODULE: " + THIS_MODULE_NAME)        
includetag = raw_input("Run Tests With Tag: ")
if includetag in (' ', ''):
    include = ' '
else:
    include = ' --include ' + includetag + ' '

excludetag = raw_input("Exclude tag: ")
if excludetag in (' ', ''):
    exclude = ' '
else:
    exclude = ' --exclude ' + excludetag + ' '

specified_browser = raw_input("Browser: ")
if specified_browser in (' ', ''):
    browser = 'gc'
else:
    browser = specified_browser


reportPath = '--report ../reports/' + includetag + '.html  '
logPath = ' --log ../reports/' + includetag + '.log.html  '
outputPath = ' --output ../reports/' + includetag + '.xml '

# Override the test data source
COMMAND = ('pybot  '
        + ' -P ../lib/:../lib_ui/:../templates/:../config/:../python/ '
        + ' --variablefile ../config/GlobalVariables_QA.py --variable BROWSER:' 
        + browser 
        + ' -L DEBUG  --exclude PRODUCTION --exclude EXCLUDE '
        + ' --consolewidth 80 '
        + ' --reporttitle IFS_TEST_SUMMARY '
        + reportPath
        + logPath
        + include
        + exclude
        + ' '  
        + outputPath
        + '  ./')

print(COMMAND)        
LOGGER.info(COMMAND)        
try:
    RETCODE = subprocess.call(COMMAND, shell=True)
    print  RETCODE
    if RETCODE < 0:
        LOGGER.info("Child was terminated by signal: " +  str(RETCODE))
        print "Child was terminated by signal: " +  str(RETCODE)
    elif RETCODE > 0:
        LOGGER.info("Child process returned error: " +  str(RETCODE))
        print "Child process returned error: " +  str(RETCODE)
except OSError, error_msg:
    LOGGER.info("Failed to complete command: " + COMMAND)
    print "Failed to complete command: " + COMMAND
    LOGGER.info(error_msg)
    print error_msg
