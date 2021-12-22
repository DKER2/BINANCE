import requests
import time, datetime
END_POINT = "https://api.binance.us"
class marketData: 
    def __init__(self, symbol,eSymbol = "USD"):
        """ 
        Source of Data for exchanging rate between a couple of assets(cryto and forex). If there is only one parameter, it is assumed that this will be converted to USD.
        :param symbol: The symbol of Cryto to be converted
        :param eSymbol: The symbol of Cryto convert to (default: USD)
        """
        self.symbol = symbol
        self.eSymbol = eSymbol
   
    def getCandlesticks(self, interval,startDate, endDate="now"):
        """
        Get Candles Data In An Specific Interval
        :param interval: The interval of an candlestick ("1m","5m","1h","5h","1d","1m","1y")
        :param startDate: The start UTC+0 Human Time in type: dd/mm/yy
        :param endDate: The end Human UTC+0 Time in type: dd/mm/yy (default: now)
        :return: return text in json type
        """
        tmpStartDate = str(int(time.mktime(datetime.datetime.strptime(startDate, "%d/%m/%Y").timetuple()))*1000)
        if endDate == "now":
            tmpEndDate = str(int(datetime.datetime.now().timestamp())*1000)
        else:
            tmpEndDate = str(int(time.mktime(datetime.datetime.strptime(endDate, "%d/%m/%Y").timetuple()))*1000)
        endPoint = END_POINT + "/api/v3/klines"
        url = endPoint + "?symbol=" + self.symbol + self.eSymbol + "&" +"interval=" + interval +"&startTime=" + tmpStartDate +"&endTime=" + tmpEndDate +"&limit=1000"
        
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

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