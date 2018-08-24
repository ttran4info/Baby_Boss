SET @campaign_id := '1704';
# Remove Ad By Child_AdGroup_ID And Child_Ad_ID
#select @ad_ids:=id from rhino.ads where ad_group_id in (select id from rhino.ad_group where campaign_id in  (select id from rhino.campaign where partner_id = @campaign_id));
delete from rhino.bidder_adgroup_assignment where adgroup_id in (select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id));
delete from rhino.gesture_ad where ad_id in (select id from rhino.ads where ad_group_id in (select id from rhino.ad_group where campaign_id in  (select id from rhino.campaign where partner_id = @campaign_id))); 

#select @ag_ids:=id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 0;
delete from rhino.ads where ad_group_id in (select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 0); 
delete from rhino.adgroup_targetlist where adgroup_id in (select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 0); 
delete from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 0; 

# Remove AdGroup By BundleID
#select @bundle_ids:=id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 1;
delete from rhino.adgroup_targetlist where adgroup_id in (select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 1); 
delete from rhino.bidder_pricing_map where adgroup_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id));
delete from rhino.adgroup_optimization where adgroup_id in ( select id from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id));
delete from rhino.ad_group where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id) and bundle = 1; 
  
# Remove Campaign By CampaignID
#select @campaign_ids:=id from rhino.campaign where partner_id = @campaign_id;
delete from rhino.campaign_taxonomy_levels where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id); 
delete from rhino.campaign_groups where campaign_id in (select id from rhino.campaign where partner_id = @campaign_id); 
delete from rhino.campaign where partner_id = @campaign_id; 


