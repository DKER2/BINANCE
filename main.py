#
#
#   TOOLS and CLASS
from binance.marketData import marketData
import json
import os
import tools.jsonProcess
import time
###
###
###


datasource  = marketData("ETH")
data = datasource.getCandlesticks("1m","20/12/2021","22/12/2021")
tools.jsonProcess.createNewJsonDataFile("ETHUSD")
tools.jsonProcess.transferDataToJsonFile(data,"ETHUSD")

