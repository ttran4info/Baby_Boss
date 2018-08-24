START TRANSACTION;
SET @partner_name := '12_REGRESSION_PARTNER%';
delete from rhino.target_list where target_placement in (select id from rhino.placement where partner_site_id in (select id from rhino.partner_site where partner_id in (select id  from rhino.partner where name like @partner_name)));
delete from rhino.placement_target_list where placement_id in (select id from rhino.placement where partner_site_id in (select id from rhino.partner_site where partner_id in (select id  from rhino.partner where name like @partner_name)));
delete from rhino.placement where partner_site_id in (select id from rhino.partner_site where partner_id in (select id  from rhino.partner where name like @partner_name));
delete from rhino.partner_site where partner_id in (select id  from rhino.partner where name like @partner_name);
delete from rhino.partner where name like @partner_name;
COMMIT;