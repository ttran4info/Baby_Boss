CREATE VIEW rhino.CP_7Day_Volume_Estimate AS (
select target_datasource_segments_id, dma, sum(count)/7 as vol_estimation 
      from rhino.segment_volume where date between DATE_SUB(now(),INTERVAL 7 DAY) and now() group by target_datasource_segments_id, dma);

CREATE VIEW rhino.CP_VOLUME_ESTIMATION_VIEW AS (
select a1.id, a1.segment_name, a1.segment_code, a1.datasource_id, a1.enabled, a2.dma, a3.dma_area, a2.vol_estimation 
from rhino.target_datasource_segments a1, rhino.CP_7Day_Volume_Estimate a2, rhino.target_geo_dma a3
where a1.id = a2.target_datasource_segments_id 
and a2.dma = a3.dma_code
);
