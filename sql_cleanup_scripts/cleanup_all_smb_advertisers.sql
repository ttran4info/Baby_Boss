delete from rhino.partner where name like 'SMB_TEST_ADVERTISER_2016_%'; 
delete from rhino.partner where name = 'SMB_DO_NOT_REMOVE' and id != 801;
delete from rhino.partner where name = 'SMB_TEST_ADVERTISER';
delete from rhino.partner where name like 'SMB_TEST_ADVERTISER_UPDATE%' and id != 772;
delete from rhino.partner where name like 'SMB_TEST_CAMPAIGN_UPDATE_ADVERTISER';
delete from rhino.partner where name = 'NULL';
delete from rhino.partner where name like '%_2016_01%';
delete from rhino.partner where name like '%TEST123%';



