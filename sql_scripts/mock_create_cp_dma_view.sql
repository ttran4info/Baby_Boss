CREATE VIEW rhino.CP_DMA_VIEW AS (
select td.id as TargetDataSourceID, 
   td.datasource_name as DataSourceName,
   td.enabled as Enabled,
   tdp.provider_name as ProviderName,
   tdp.enabled as ProviderEnabled, 
   tds.id as SegmentID,
   tds.segment_name as SegmentName,
   tds.segment_code as SegmentCode,
   tds.created_dt as SegmentCreateDate,
   tds.modified_dt as SegmentModifiedDate,
   tds.enabled as SegmentEnabled
from 
   rhino.target_datasource td, 
   rhino.target_datasource_provider tdp,
   rhino.target_datasource_segments tds 
where 
   td.provider_id = tdp.id
and 
   tds.datasource_id = td.id
);