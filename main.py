#
#
#   TOOLS and CLASS
from binance.marketData import marketData
import tools.jsonProcess
import json
###
###
###
########
### Current Endate is 1640765841000
#########  DO NOT DELETE






cryptos = ['ADA','ATOM','AVAX','BNB','BTC','CRV','DOGE','ETH','FTM','GRT','HBAR','LINK','MANA','MATIC','OMG','ONE','SOL','SUSHI','VET','ZIL']
startDates = [1523937720000, 1556510400000, 1600756200000, 1509940440000, 1502942400000, 1597464000000, 1562328000000, 1502942400000, 1560225600000, 1608237000000, 1569729600000, 1547632800000, 1596708000000, 1556290800000, 1554264000000, 1559361600000, 1597125600000, 1598958000000, 1532491200000, 1550574240000]



crypto = 'DOGE'
data_soure = marketData(crypto)
data_soure.getCandlesticks("1d","1609459200000","1640908800000")

# for i in range(20):
#     crypto = cryptos[i]
#     print(crypto + ':')
#     u =0
#     with open ("./data/"+crypto+"USDT"+".json") as f: 
#         tmp = json.loads(f.read())
#     for i in range(len(tmp)-1):
#         if tmp[i+1][0] - tmp[i][0] != 60000:
#             u = u +1
#     print(u)
# crypto='CRV'
# endDate = "1640765841000" 
# startDate= "1530033660000"
# data_source = marketData(crypto)

# flag = True
# ErrorIndex = -1

# endDate = "1640765841000" 
# startDate= str(startDates[i])
# data_source = marketData(crypto)
#     while startDate<endDate:
#         tmp = json.loads(data_source.getCandlesticks("1m",startDate,endDate))
#         tmpEndDate = tmp[len(tmp)-1][0]
#         startDate = str(tmpEndDate +60000)




