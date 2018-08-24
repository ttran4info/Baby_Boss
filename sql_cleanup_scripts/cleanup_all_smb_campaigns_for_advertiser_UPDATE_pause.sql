SET @partner_id := '772';
update rhino.ad_group set status = 2 where campaign_id in (select id from rhino.campaign where partner_id = @partner_id); 
  

