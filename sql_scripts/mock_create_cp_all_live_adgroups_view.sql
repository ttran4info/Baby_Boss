CREATE VIEW rhino.CP_ALL_LIVE_ADGROUPS AS (
select 
adGroup.id as adGroup_table_id, adGroup.name, adGroup.start_date, adGroup.end_date, adGroup.units_sold, adGroup.units_delivered, 
adGroup.cost_per_unit, adGroup.delivered_impressions, adGroup.delivered_clicks, adGroup.delivered_acquisitions, 
adGroup.budget, adGroup.pacing_id, adGroup.exclusive, adGroup.guaranteed, adGroup.remnant, adGroup.remnant_external, 
adGroup.house, adGroup.status, adGroup.created_dt, adGroup.modified_dt, adGroup.campaign_id, adGroup.frequency_cap_id, 
adGroup.ad_group_payment_type_id, adGroup.bonus_parent_ad_group_id, adGroup.ecpm, adGroup.optimize_bundle, 
adGroup.bundle_parent_id, adGroup.bundle, adGroup.weight, adGroup.allocation, adGroup.custom_dates, adGroup.custom_frequency_cap, 
adGroup.custom_targeting, adGroup.time_zone, adGroup.time_zone_user, adGroup.ui_weight, adGroup.test_ads, 
adGroup.ip_to_geo_allowed_type, adGroup.pacing_units_sold, adGroup.pacing_units_delivered, adGroup.pacing_start_date, 
adGroup.pacing_end_date, adGroup.pacing_recalculation, adGroup.ad_text, adGroup.track_client_impression, adGroup.use_spoc_targeting, 
adGroup.requires_raw_device_id, adGroup.app_id, adGroup.use_placeiq, adGroup.daily_cap_enabled, adGroup.daily_cap_units_sold, adGroup.daily_cap_units_delivered, 
c.id as c_id, c.partner_id as c_partner_id, c.name as c_Name, c.start_time as c_start_time, c.end_time as c_end_time, c.impressions_sold as c_impressions_sold, c.impressions_delivered as c_impressions_delivered, 
c.budget as c_budget, c.status as c_status, c.insertion_order as c_insertion_order, c.created_dt as c_created_dt, c.modified_dt as c_modified_dt, c.keywords as c_keywords
from rhino.ad_group as adGroup, rhino.campaign c 
where c.status=1 and c.start_time < now()
and c.end_time > now() and adGroup.status=1 and adGroup.start_date < now() and adGroup.end_date > now()
and ((adGroup.units_delivered <= adGroup.units_sold) or adGroup.units_sold is null or adGroup.units_sold=0)
and adGroup.bundle=false and adGroup.test_ads=0
); 


CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `rhino`@`%` 
    SQL SECURITY DEFINER
VIEW `CP_LIVE_ADGROUPS_WITH_NOPLACEMENT_TARGETING` AS
    select 
        `adgroup_targetlist`.`adgroup_id` AS `adgroup_id`
    from
        `adgroup_targetlist`
    where
        ((`adgroup_targetlist`.`target_list_id` = 398)
            and `adgroup_targetlist`.`adgroup_id` in (select 
                `CP_ALL_LIVE_ADGROUPS`.`adGroup_table_id`
            from
                `CP_ALL_LIVE_ADGROUPS`));

