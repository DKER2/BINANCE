from binance.client import Client
from binance.marketData import marketData
import tools.jsonProcess
import json
END_POINT = "https://api.binance.us"
# #TRASH API
# API_KEY= "BlauCq9caQqSBHp1txb8eR2QYbay3U9xqnzrLn6EqOo1A7D7PIFwAsw8mZL47bvj"
# API_SIGN ="GKe8xqlfynUq3ALvK4r0V628knVD6V53Qo3dC9Jd5iczbeSLrVyKbMKx8eP5GCJw"
# #TRASH API
dataSoure = marketData("BTC","USDT")
data = dataSoure.getOrderBook("1638353410000","1638439810000",'1m')
tools.jsonProcess.createNewJsonDataFile("BTCUSDT")
tools.jsonProcess.transferDataToJsonFile(data,"BTCUSDT.json")
tools.jsonProcess.clearDataInJsonFile("BTCUSDT.json")