START TRANSACTION;
SET @campaign_name := '04_FREQCAP_CAMPAIGN%';
delete from rhino.bidder_adgroup_assignment where adgroup_id in (select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name));
delete from rhino.gesture_ad where ad_id in (select id from rhino.ads where ad_group_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name)));
delete from rhino.ads where ad_group_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name));
delete from rhino.adgroup_targetlist where adgroup_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name));
delete from rhino.bidder_pricing_map where adgroup_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name));
delete from rhino.adgroup_optimization where adgroup_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name));
delete from rhino.ad_group where campaign_id in (select id from rhino.campaign where name like @campaign_name);
delete from rhino.campaign_taxonomy_levels where campaign_id in (select id from rhino.campaign where name like @campaign_name);
delete from rhino.campaign_adgroup_visibility where campaign_id in (select id from rhino.campaign where name like @campaign_name);
delete from rhino.campaign_groups where campaign_id in (select id from rhino.campaign where name like @campaign_name);
delete from rhino.campaign where name like @campaign_name;
COMMIT;