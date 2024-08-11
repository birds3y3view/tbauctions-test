select 
	fb.auction_id,
	da.auction_type, 
	count(fb.auction_id) 
from 
	reporting.fact_bids fb, 
	reporting.dim_auction da 
where 
	fb.auction_id = da.auction_id 
group by 
	fb.auction_id,
	da.auction_type;