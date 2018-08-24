"""
Copyright 2012 4Info 
Generic Robot Framework Test Runner
"""

import  subprocess
import  os
import logging
import sys
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

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Arg1:', str(sys.argv[1])

report_tag_name = 'RegressionTests'
try:
    #includetag = raw_input("Run Tests With Tag: ")
    includetag = str(sys.argv[1])
    if includetag in (' ', ''):
        include = ' '
    else:
        include = ' --include ' + includetag + ' '
except OSError, error_msg:
    print "No Include tag given, defaulting to running all tests..."
    include = ' '
    print error_msg
    
try:
    #excludetag = raw_input("Exclude tag: ")
    excludetag = str(sys.argv[2])
    if excludetag in (' ', ''):
        exclude = ' '
    else:
        exclude = ' --exclude ' + excludetag + ' '
except OSError, error_msg:
    print "No exclude tag given, defaulting to no exclude..."
    exclude = ' '
    print error_msg



reportPath = '--report ../reports/' + report_tag_name + '.html  '
logPath = ' --log ../reports/' + report_tag_name + '.log.html  '
outputPath = ' --output ../reports/' + report_tag_name + '.xml '

# Override the test data source
COMMAND = ('pybot  '
        + ' -P ../lib/:../lib_ui/:../templates/:../config/:../python/ '
        + ' --variablefile ../config/GlobalVariables_PROD.py'
        + ' -L DEBUG '
        + ' --consolewidth 100 '
        + reportPath
        + logPath
        + include
        + exclude
        + '  --exclude  EXCLUDE  --exclude WIP  --exclude PARTNERS_SEARCH --exclude GEO_HISTORY  --exclude PRODUCTION  --exclude MOCK_DATABASE_SETUP  --exclude Known_Issue  --exclude PRIZM  --exclude CONNEXIONS  ' 
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
