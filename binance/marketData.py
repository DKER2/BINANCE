import requests
import json
import os.path
from requests.models import REDIRECT_STATI
from tools import jsonProcess
import time, datetime
END_POINT = "https://api.binance.com"
class marketData:
    def __init__(self, symbol,eSymbol = "USDT"):
        """ 
        Source of Data for exchanging rate between a couple of assets(cryto and forex). If there is only one parameter, it is assumed that this will be converted to USD.
        :param symbol: The symbol of Cryto to be converted
        :param eSymbol: The symbol of Cryto convert to (default: USD)
        """
        self.symbol = symbol
        self.eSymbol = eSymbol
   
    def getCandlesticks(self, interval,startDate, endDate="now"):
        """
        Get Candles Data In An Specific Interval With Limit 1000 Candle
        :param interval: The interval of an candlestick ("1m","5m","1h","5h","1d","1m","1y")
        :param startDate: The start UTC+0 Human Time in type: timestamp format
        :param endDate: The end Human UTC+0 Time in type: timestamp format (default: now)
        :return: return text in json type
        """
        # tmpStartDate = str(int(time.mktime(datetime.datetime.strptime(startDate, "%d/%m/%Y - %H:%M:%S").timetuple()))*1000)
        if endDate == "now":
            tmpEndDate = str(int(datetime.datetime.now().timestamp())*1000)
        # else:
        #     tmpEndDate = str(int(time.mktime(datetime.datetime.strptime(endDate, "%d/%m/%Y - %H:%M:%S").timetuple()))*1000)
        endPoint = END_POINT + "/api/v3/klines"
        url = endPoint + "?symbol=" + self.symbol + self.eSymbol + "&" +"interval=" + interval +"&startTime=" + startDate  +"&endTime=" + endDate +"&limit=1000"
        
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        if os.path.exists('./data/'+self.symbol+self.eSymbol+".json"): 
            jsonProcess.deleteLastCharacterInJsonFile(self.symbol+self.eSymbol)
            jsonProcess.transferDataToJsonFile(","+response.text[1:],self.symbol+self.eSymbol)
        else:
            jsonProcess.transferDataToJsonFile(response.text,self.symbol+self.eSymbol)
        
        return response.text
     
    def getRecentTrade(self):
        """
        :return: return new trade in text in json type
        """
        endPoint = END_POINT + "/api/v3/trades"
        url = endPoint + "?symbol=" + self.symbol + self.eSymbol 
        
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.text
    
### DEVELOPING
    def realTimeUpdating(self): 
        tmpEndDate = str(int(datetime.datetime.now().timestamp())*1000)
        while True: 
            self.getCandlesticks("1m","")
### DEVELOPING


### Need to comment
    def testCandleData(self):
        flag = True
        ErrorIndex = -1
        with open ("./data/"+self.symbol+self.eSymbol+".json") as f: 
            tmp = json.loads(f.read())
        for i in range(len(tmp)-1):
            if tmp[i+1][0] - tmp[i][0] != 60000:
                flag = False
                ErrorIndex = i
                break
        return flag, ErrorIndex
### Need to comment