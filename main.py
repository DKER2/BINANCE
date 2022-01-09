#
#
#   TOOLS and CLASS
from binance.marketData import marketData
import json
import os
import tools.jsonProcess
import time,datetime
###
###
###
########
### Current Endate is 1640765841000
#########  DO NOT DELETE



###MATIC 2021 SUSHI 29/8/2020 ADA 10/8/2017 FTM 2021 CRV 15/08/2020 MANA 2021 VET 2020 LINK 2019 ONE 6/4/2019 DOGE 2021 AVAX 2021 HBAR 08/09/2019 ZIL 27/01/2018 GRT 04/01/2021 OMG 16/07/2017









crypto = "BTC"
endDate = "03/01/2022 - 17:14:00" 
startDate= "03/01/2022 - 12:00:00"
data_source = marketData(crypto,"USDT")
data_source.getCandlesticks("1m",startDate,endDate)


while startDate<endDate:
    startDate = str(int(startDate) + 60000000)
    data = data_source.getCandlesticks("1m",startDate,endDate)
    tools.jsonProcess.deleteLastCharacterInJsonFile(crypto+"USD")
    tools.jsonProcess.transferDataToJsonFile(','+data[1:],crypto+"USD")
    

    


