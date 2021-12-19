from binance.marketData import marketData
import tools.jsonProcess
import time

# #TRASH API
# API_KEY= "BlauCq9caQqSBHp1txb8eR2QYbay3U9xqnzrLn6EqOo1A7D7PIFwAsw8mZL47bvj"
# API_SIGN ="GKe8xqlfynUq3ALvK4r0V628knVD6V53Qo3dC9Jd5iczbeSLrVyKbMKx8eP5GCJw"
# #TRASH API
dataSoure = marketData("SOL")
data = dataSoure.getCandlesticks("5m","13/12/2021")
print(data)
count = 0
while count < 2:
    
    data = dataSoure.getCandlesticks("5m","13/12/2021")
    tools.jsonProcess.createNewJsonDataFile("SOLUSDT")
    tools.jsonProcess.transferDataToJsonFile(data,"SOLUSDT")
    time.sleep(300)
    count += 1
    print(count)
    
print(count)
