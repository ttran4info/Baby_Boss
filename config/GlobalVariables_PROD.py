
"""
Copyright 2012 4Info 
Global variables used for testing.  
The values in here are the default values and can be overriden within the tests.
"""
#ENVIRONMENT = "QA"
ENVIRONMENT = "PROD"
LOG_SETTING = "0"

#QA_URL= "http://qa-adui1:8080/adhaven-ui/"
#104.239.188.235 = manage-east.adhaven.com
QA_URL= "https://manage-east.adhaven.com/adhaven-ui/"
#QA_DEFAULT_USER = "admin@4info.com"
#QA_DEFAULT_PASSWORD = "test1234"
QA_DEFAULT_USER = "ttran@4info.com"
QA_DEFAULT_PASSWORD = "changeme"

# "GiKzMv4w"
QA_REPORTING_USER = "Reporting@4info.com"
QA_REPORTING_PASSWORD = "Reporting1"


"""The settings below allows tests to just use USER, PASSWORD, URL 
and run against any environment.  This can be manually set in this 
GlobalVariables.py file or passed in from the test start command.  
Tests could also override these values during run-time and change the environment.
"""
USER = QA_DEFAULT_USER
PASSWORD = QA_DEFAULT_PASSWORD
URL = QA_URL

"""jboss 5 ad-engine, jboss 7 use events"""
EXTERNAL_EVENT_ENGINE = "events201:8080" #"e.adhaven.com"
EVENT_URL = "http"              #https
EVENT_PATH= EVENT_URL + "://" + EXTERNAL_EVENT_ENGINE + "/events/event"
#EVENT_PATH= "http://qa-engine-06/events/event"
LOG_PATH = "~/server/4info/log"
#This is the internal event engine that we ssh into to look (even if event is external address, we need internal address to ssh into)
EVENT_ENGINE = "events201"          #;events202;events203;events204;events205;events206" #10.34.64.101
BID_ENGINE = "rtb201"  #10.34.68.14
BID_ENGINE_ONE = "rtb201"        #10.34.68.14

SSH_HOST = EVENT_ENGINE
SSH_RTB_HOST = BID_ENGINE
SSH_USER = "jboss"
SSH_PASS = "a5QwVtUkYDQu"
SSH_HOST2 = "qa-engine2"
LOAD_BALANCER_HOST = "172.16.7.204"

# TRUSTe ETL 
TRUSTE_HOST = "10.18.8.23"   #qa-ui-10
TRUSTE_SSH_USER = "tpreports"
TRUSTE_SSH_PASS = "reporting4Duty!"


DEFAULT_AUDIENCE_ENGINE = "qa-engine-10"
#DEFAULT_AUDIENCE_ENGINE = "qa-engine-05"
AUDIENCE_ENGINE2 = "qa-engine-12"
#AUDIENCE_ENGINE2 = "qa-engine-05"
PRIZM_05_PLACEMENTID = "77"
PRIZM_06_PLACEMENTID = "78"
PRIZM_07_PLACEMENTID = "79"
PRIZM_08_PLACEMENTID = "80"
PRIZM_09_PLACEMENTID = "81"

CONNEX_05_PLACEMENTID = "82"
CONNEX_06_PLACEMENTID = "83"
CONNEX_07_PLACEMENTID = "84"
CONNEX_08_PLACEMENTID = "85"
CONNEX_09_PLACEMENTID = "86"


PLACEMENT_DISABLED_ID = "87"
PLACEMENT_LIVE_ID = "88"
PLACEMENT_TEST_ID = "89"

PLACEMENT_EDIT_ID = "90"
PLACEMENT_EDIT_NAME = "PLACEMENT_EDIT"

DEFAULT_PLACEMENT = "76"
DEFAULT_MOPUB_APP_PLACEMENT = "8331"

DEFAULT_MOPUB_APP_PLACEMENT_ONLINE="9500"

PARTNER_SEARCH_PLACEMENT_ID_1 = PRIZM_05_PLACEMENTID
PARTNER_SEARCH_PLACEMENT_NAME_1 = "PRIZM_01"

PARTNER_SEARCH_PLACEMENT_ID_2 = PLACEMENT_EDIT_ID 
PARTNER_SEARCH_PLACEMENT_NAME_2 = PLACEMENT_EDIT_NAME 

#AD_ENGINE_REVISION_URL = "http://" + DEFAULT_AUDIENCE_ENGINE + ":8080/ad-engine/svn_revision"
AD_ENGINE_REVISION_URL = "http://" + EVENT_ENGINE + ":8080/events/svn_revision"
AD_UI_REVISION_URL =  URL + "/svn_revision"
HOUSEHOLD_REVISION_URL = "http://10.18.8.23:8080/household/svn_revision"   # qa-ui-10 10.18.8.23
ACE_REVISION_URL =  "http://10.18.8.30:8080/ace7/svn_revision"  #qa-ace-10 10.18.8.30

GEO_SERVICES_URL = "http://archive10:8080/geonames/servlet/geonames?srv=findNearbyAddress&lat=37.786121&lng=-122.405303"
PLACEIQ_SERVICES_URL = "http://api-west.placeiq.com/services/rest/placeScore/4INFO?format=json&taxonomy=4INFO&lat=40.7619&lng=-73.9763&key=f7d74420-59a9-11e0-80e3-0800200c9a66"


"""SQL DATABASE CONNECTIONS"""
DB_API_MODULE_NAME    = "MySQLdb"
DB_NAME_RHINO         =  "rhino"
DB_USER               =  "rhino"
DB_PASSWORD           =  "rhino"
DB_HOST               =  "adhdb"   # adhdb
DB_PORT               =  "3306"


# ADVERTISER INFORMATION
DEFAULT_ADVERTISER = "04_TEST_ADVERTISER"
DEFAULT_ADVERTISER_ID = 183 
DEFAULT_API_KEY = "96a3be339dc3269b"
REGRESSION_ADVERTISER= "QA_REGRESSION"
REGRESSION_TIMEZONE= "GMT"
REGRESSION_START_DATE= "6/11/2015"
REGRESSION_END_DATE= "6/11/2018"

#      http://qa-engine1:8080/AdHavenRest/v2/reporting/advertiser?advertiserId=357
#      &reportId=CampaignPerformanceOverall&campaignId=679&startDate=20130301
#      &endDate=20130311&groupTimeFrame=DAY&outputFormat=xls&timeZone=GMT[+00:00]
REPORTING_RESTAPI_ENGINE = "qa-engine1"
REPORTING_API_PREFIX = "http://" + REPORTING_RESTAPI_ENGINE + ":8080/AdHavenRest/v2/reporting/" 


# RTB 
RTB_HOST = "http://" + BID_ENGINE + ":8080"   #rtb204
RTB_ADAPTV_API = "f68e46bc869e960e"
RTB_AOL_API = "9b673680f53afa00"
RTB_APPNEXUS_API =  "cc2f0bbaf30cdb0f"
RTB_BRX_API= "4a1f4e830641bcbe"
RTB_INNERACTIVE_API = "f00e01437e0f2fb2"
RTB_MOPUB_API = "42ba406a62ec13ca"
RTB_NEXAGE_API = "739ae7c9f881d65f"
RTB_OPERAMW_API = "d4a6c5ab985b9dd0"
#RTB_PUBMATIC_API = "e493573f9b2f9a0b"
RTB_RUBICON_API = "dbf412f8bf9de753"
RTB_SMAATO_API = "113e4d18744754b6"
RTB_VDOPIA_API = "a906ed33d56f4ee5"
RTB_LIVERAIL_API = "9615ce569d00b743"
RTB_SPOTXCHANGE_API= "19543f2b13f14db3a71c64c258228b8a"
RTB_XAD_API = "65260410174948b5b5ba6f4532b55960"
#Turning Clear Device ID  = ON or OFF (use mostly for RTB testing along with Device ID
CLEAR_ID = "ON"
HASHED_ID = "ON"

# Geofence 
GEOFENCE_PERF_PLACEMENTID = "6480"

# SMB - qa-smb-01
#SMB_EXTERNAL_HOST = "http://12.226.103.145"
#SMB_QA_HOST_01 = "http://qa-smb-01:8080"

SMB_QA_HOST_02 = "http://10.18.8.29:8080"
#SMB_QA_HOST_02 = "http://172.16.5.72:8080"
#   PING qa-smb-02.corp.4info.net (172.16.5.72) 
# qq-smb-10    10.18.8.29
SMB_HOST = "http://10.18.8.29:8080"

SMB_AUTH = "Basic c21iX3VzZXJzQDRpbmZvLmNvbTp0ZXN0MTIzNA=="
SMB_USER = "smb_users@4info.com"
SMB_USER_PW = "test1234"

SMB_AUTH_Reporting = "Basic cWFAdGVzdC5jb206MTIzNDU2Nzg="
SMB_AUTH_Admin = "Basic YWRtaW5ANGluZm8uY29tOnRlc3QxMjM0"

SMB_DEFAULT_ADVERTISER="486"
SMB_DEFAULT_ADVERTISER_UPDATE="772"
SMB_DEFAULT_ADVERTISER_END2END="714"
SMB_DO_NOT_REMOVE="801"
SMB_DEFAULT_PLACEMENT_TARGET_LIST_ID="207047"
