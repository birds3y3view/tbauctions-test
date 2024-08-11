select
	fb.auction_id,
	di.item,
	count(fb.auction_id)
from 
	reporting.fact_bids fb,
	reporting.dim_item di
where
	fb.item_id = di.item_id
group by
	fb.auction_id,
	di.item;