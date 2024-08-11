SELECT b.auction_id, b.datetime, b.bid, bu.id as "bidder_id", b.open_bid, b.price, b.item_id   
FROM clean.bids AS b
INNER JOIN clean.buyers AS bu ON b.bidder = bu.username