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
include = 'RegressionTests'
exclude = ' --exclude  EXCLUDE  --exclude REPORTING --exclude WIP  --exclude PRODUCTION  --exclude PARTNERS_SEARCH  --exclude MOCK_DATABASE_SETUP  --exclude GEO_HISTORY  --exclude Known_Issue --exclude PRIZM  --exclude CONNEXIONS'

reportPath = '--report ../reports/' + include + '.html  '
logPath = ' --log ../reports/' + include + '.log.html  '
outputPath = ' --output ../reports/' + include + '.xml '

# Override the test data source
COMMAND = ('pybot  '
        + ' -P ../lib/:../lib_ui/:../templates/:../config/:../python/ '
        + ' --variablefile ../config/GlobalVariables_QA.py'
        + ' -L DEBUG '
        + reportPath
        + logPath
        + exclude
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
