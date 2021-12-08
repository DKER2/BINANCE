from binance.client import Client
END_POINT = "https://api.binance.us/api/v3/historicalTrades?symbol=BTCUSDT"
API_KEY= "BlauCq9caQqSBHp1txb8eR2QYbay3U9xqnzrLn6EqOo1A7D7PIFwAsw8mZL47bvj"
API_SIGN ="GKe8xqlfynUq3ALvK4r0V628knVD6V53Qo3dC9Jd5iczbeSLrVyKbMKx8eP5GCJw"
text = Client(API_KEY,API_SIGN,END_POINT)



