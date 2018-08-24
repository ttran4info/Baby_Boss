
"""
Copyright 2012 4Info
Global variables used for testing.
The values in here are the default values and can be overriden within the tests.
"""
ENVIRONMENT = "QA"
#ENVIRONMENT = "PROD"
LOG_SETTING = "0"

#QA_URL= "http://qa-adui1:8080/adhaven-ui/"
QA_UI_SERVER = "qa-ui-10"
#QA_URL= "http://" + QA_UI_SERVER + ":8080/adhaven-ui/"
QA_URL= "https://qa-ui-cluster.adhaven.com/adhaven-ui/"
QA_DEFAULT_USER = "admin@4info.net"
QA_CATALINA_USER = "regression@catalina.com"                            #Editor
QA_CATALINA_USER2 = "regression2@catalina.com"                          #Basic
QA_CATALINA_USER3 = "regression3@catalina.com"                          #Custom Write only (which should allow read/write)
QA_CATALINA_AND_QA_USER = "regression_catalina_and_qa@catalina.com"     #Editor/Editor
QA_CATALINA_AND_QA_USER2 = "regression_catalina_and_qa2@catalina.com"   #Editor/Basic
QA_CATALINA_AND_QA_USER3 = "regression_catalina_and_qa3@catalina.com"   #Basic/Editor
QA_QA_USER = "regression_qa@qa.com"                                     #Editor
QA_INACTIVE_USER = 'regression_inactive@catalina.com'
QA_READONLY_USER='regression_qa_readonly@qa.com'                        #Admin read only user
QA_UNDERTONE_USER='regression_undertone@undertone.com'
QA_DEFAULT_PASSWORD = "P@ssw0rd"
# "GiKzMv4w"
QA_REPORTING_USER = "Reporting@4info.com"
QA_REPORTING_PASSWORD = "Reporting1"

QA_API_EXTERNAL="qa-api.4info.com"
QA_API_EXTERNAL_PROXY="qa-api-proxy.4info.com"
QA_API_EXTERNAL_PORT="443"

QA_PHOENIX="qa-campaigns.4info.com"
QA_PHOENIX_PORT="443"

QA_KONG = "api-gateway.qa.adhaven.com" #10.18.8.101
QA_KONG_PORT = "8000"

# QA_KONG = "dev-dswarm-01.ahprod.adhaven.com" #10.18.8.101
# QA_KONG_PORT = "80"

QA_DOCKER = "qa-docker-slave-10"

QA_USER_MANAGEMENT=QA_API_EXTERNAL_PROXY        #QA_KONG       #"qa-api.4info.com"(https)              #"qa-docker-slave-10.adhaven.com"
QA_USER_MANAGEMENT_PORT=QA_API_EXTERNAL_PORT      #"443"(https)                #QA_KONG_PORT           #"8443"

QA_USER_MANAGEMENT_HTTP=QA_KONG                           #"qa-dswarm-01"
QA_USER_MANAGEMENT_PORT_HTTP=QA_KONG_PORT                       #"18071"         #QA_KONG_PORT      #"8090"

QA_PAC =QA_API_EXTERNAL_PROXY                         # "qa-dswarm-01"           #QA_KONG        ""
QA_PAC_PORT =QA_API_EXTERNAL_PORT               # "18082"             #QA_KONG_PORT  #"8000"        qa-dswarm-01:18082

QA_INVENTORY=QA_API_EXTERNAL_PROXY                    #"qa-dswarm-01" #QA_KONG
QA_INVENTORY_PORT=QA_API_EXTERNAL_PORT        #"58082" #QA_KONG_PORT    #"8000"

QA_ELASTIC = "qa-elastic-01"
QA_ELASTIC_PORT = "9200"

QA_ACE=QA_API_EXTERNAL_PROXY                #"qa-dswarm-01.qa.adhaven.com" #10.18.8.101
QA_ACE_PORT=QA_API_EXTERNAL_PORT      #"18090""

QA_HYDRA=QA_API_EXTERNAL_PROXY                #"qa-hydra-10"
QA_HYDRA_PORT=QA_API_EXTERNAL_PORT
# HYDRA_AUTH="Basic YWRtaW5ANGluZm8ubmV0OjE2ZDdhNGZjYTc0NDJkZGEzYWQ5M2M5YTcyNjU5N2U0"
HYDRA_AUTH="Basic YWRtaW5ANGluZm8ubmV0OjE2MWViZDdkNDUwODliMzQ0NmVlNGUwZDg2ZGJjZjky"
#"Basic Y3BoYW1ANGluZm8uY29tOjVmYjlmYzA2ZTRmODhhNzg2YmEwYTU5MDE1NDVkNzQy"

#For use of audience solution
QA_API_EXTERNAL_GCP="qa-api-proxy-gcp-deployment-api.4info.com"
QA_API_EXTERNAL_GCP_PORT="443"

QA_DEPLOYMENT=QA_API_EXTERNAL_GCP
QA_DEPLOYMENT_PORT=QA_API_EXTERNAL_GCP_PORT

"""The settings below allows tests to just use USER, PASSWORD, URL
and run against any environment.  This can be manually set in this
GlobalVariables.py file or passed in from the test start command.
Tests could also override these values during run-time and change the environment.
"""

USER = QA_DEFAULT_USER
PASSWORD = QA_DEFAULT_PASSWORD
URL = QA_URL

"""jboss 5 ad-engine, jboss 7 use events"""
EXTERNAL_EVENT_ENGINE = "qa-events-svcolo.adhaven.com"
EVENT_URL = "https"
EVENT_PATH= EVENT_URL + "://" + EXTERNAL_EVENT_ENGINE + ":443/events/event"
#EVENT_PATH= "http://qa-engine-06/events/event"
LOG_PATH = "~/server/4info/log"
#This is the internal event engine that we ssh into to look (even if event is external address, we need internal address to ssh into)
EVENT_ENGINE = "qa-events-10;qa-events-11" #10.18.8.6;10.18.8.7
BID_ENGINE = "qa-rtb-10;qa-rtb-11"         #10.18.8.8;10.18.8.9
BID_ENGINE_ONE = "qa-rtb-11"    #"35.227.74.61" #                #10.18.8.8
QA_CACHE_SERVER = "qa-cache-server-10"

SSH_HOST = EVENT_ENGINE
SSH_RTB_HOST = BID_ENGINE
SSH_USER = "jboss"
SSH_PASS = "lebowski"
SSH_HOST2 = "qa-engine2"
LOAD_BALANCER_HOST = "172.16.7.204"

#Adpickup
AD_PICKUP_ENGINE = "qa-adpickup-10"
#AD_PICKUP_URL = "https://" + AD_PICKUP_ENGINE + ":8080/bid-notice/notify/media"
AD_PICKUP_URL = "https://qa-adpickup.adhaven.com/bid-notice/notify/media"

# TRUSTe ETL
TRUSTE_HOST = "qa-ui-10"   #10.18.8.23
TRUSTE_SSH_USER = "tpreports"
TRUSTE_SSH_PASS = "reporting4Duty!"


DEFAULT_AUDIENCE_ENGINE = "qa-ui-10"
#DEFAULT_AUDIENCE_ENGINE = "qa-engine-05"
#AUDIENCE_ENGINE2 = "qa-engine-12"
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
AD_UI_REVISION_URL =  URL + "version"
HOUSEHOLD_REVISION_URL = "http://qa-ui-10:8080/household/svn_revision"   #  10.18.8.23
ACE_REVISION_URL =  "http://qa-ace-10:8080/ace7/svn_revision"  # 10.18.8.30

GEO_SERVICES_URL = "http://archive10:8080/geonames/servlet/geonames?srv=findNearbyAddress&lat=37.786121&lng=-122.405303"
PLACEIQ_SERVICES_URL = "http://api-west.placeiq.com/services/rest/placeScore/4INFO?format=json&taxonomy=4INFO&lat=40.7619&lng=-73.9763&key=f7d74420-59a9-11e0-80e3-0800200c9a66"


"""SQL DATABASE CONNECTIONS"""
DB_API_MODULE_NAME    = "MySQLdb"
DB_NAME_RHINO         =  "rhino"
DB_USER               =  "rhino_auto"
DB_PASSWORD           =  "rhino"
DB_HOST               =  "qa-db.qa.adhaven.com"   # 10.18.8.21
# DB_HOST               = "192.168.10.40" #"qa-db.qa.adhaven.com"   # 10.18.8.21
DB_HOST_IO          =   "qa-io-db-master.corp.4info.net"
DB_PORT =  "3306"

# ADVERTISER INFORMATION
DEFAULT_ADVERTISER = "QA_REGRESSION_TESTS"
DEFAULT_ADVERTISER_ID = 274     #183
DEFAULT_API_KEY = "96a3be339dc3269b"
REGRESSION_ADVERTISER= "QA_REGRESSION"
REGRESSION_TIMEZONE= "GMT"
REGRESSION_START_DATE= "06/11/2015"
REGRESSION_END_DATE= "06/11/2019"
REGRESSION_EXPIRED_START_DATE_DB="2016-06-11 23:59:59"
REGRESSION_EXPIRED_END_DATE_DB="2017-06-11 23:59:59"

#      http://qa-engine1:8080/AdHavenRest/v2/reporting/advertiser?advertiserId=357
#      &reportId=CampaignPerformanceOverall&campaignId=679&startDate=20130301
#      &endDate=20130311&groupTimeFrame=DAY&outputFormat=xls&timeZone=GMT[+00:00]
REPORTING_RESTAPI_ENGINE = "qa-engine1"
REPORTING_API_PREFIX = "http://" + REPORTING_RESTAPI_ENGINE + ":8080/AdHavenRest/v2/reporting/"


# RTB
RTB_HOST = "http://"+ BID_ENGINE_ONE + ":8080"
#RTB_HOST = "http://qa-rtb.adhaven.com"
RTB_ADAPTV_API = "f68e46bc869e960e"
RTB_AOL_API = "9b673680f53afa00"
RTB_APPNEXUS_API =  "cc2f0bbaf30cdb0f"
#RTB_BRX_API= "4a1f4e830641bcbe"
RTB_INNERACTIVE_API = "f00e01437e0f2fb2"
RTB_MOPUB_API = "42ba406a62ec13ca"
RTB_NEXAGE_API = "739ae7c9f881d65f"
RTB_OPERAMW_API = "d4a6c5ab985b9dd0"
RTB_PUBMATIC_API = "e493573f9b2f9a0b"
RTB_OPENX_API = "377c7998bb9f42e5aea0416c9dac091f"
RTB_RUBICON_API = "dbf412f8bf9de753"
RTB_SMAATO_API = "113e4d18744754b6"
RTB_VDOPIA_API = "a906ed33d56f4ee5"
RTB_LIVERAIL_API = "9615ce569d00b743"
RTB_SPOTXCHANGE_API= "19543f2b13f14db3a71c64c258228b8a"
RTB_XAD_API = "65260410174948b5b5ba6f4532b55960"
RTB_ADX_API = "59725dddbfd04e75827b81ecc7ee7f29"
#Turning Clear Device ID  = ON or OFF (use mostly for RTB testing along with Device ID
#CLEAR_ID = "ON"
HASHED_ID = "ON"

# Geofence
GEOFENCE_PERF_PLACEMENTID = "6480"

# SMB - qa-smb-01
#SMB_EXTERNAL_HOST = "http://12.226.103.145"
#SMB_QA_HOST_01 = "http://qa-smb-01:8080"

SMB_QA_HOST_02 = "http://qa-smb-10:8080" #10.18.8.29:8080"
#SMB_QA_HOST_02 = "http://172.16.5.72:8080"
#   PING qa-smb-02.corp.4info.net (172.16.5.72)
# qq-smb-10    10.18.8.29
SMB_HOST = "http://qa-smb-10:8080" #10.18.8.29:8080"

#SMB_AUTH = "Basic c21iX3VzZXJzQDRpbmZvLmNvbTp0ZXN0MTIzNA=="
#SMB_USER = "smb_users@4info.com"
#SMB_USER_PW = "test1234"
SMB_AUTH = "Basic YWRtaW5ANGluZm8ubmV0OnRlc3QxMjM0"
SMB_USER = "admin@4info.net"
SMB_USER_PW = "test1234"


SMB_AUTH_Reporting = "Basic cWFAdGVzdC5jb206MTIzNDU2Nzg="
SMB_AUTH_Admin = "Basic YWRtaW5ANGluZm8uY29tOnRlc3QxMjM0"

SMB_DEFAULT_ADVERTISER="922"
SMB_DEFAULT_ADVERTISER_UPDATE="772"
SMB_DEFAULT_ADVERTISER_END2END="922"
SMB_DO_NOT_REMOVE="801"
SMB_DEFAULT_PLACEMENT_TARGET_LIST_ID="207047"


APPNEXUS_FLAG="RTB"
