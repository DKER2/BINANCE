import requests
END_POINT = "https://api.binance.us"
class marketData: 
    def __init__(self, symbol,eSymbol):
        """ 
        :param symbol: The symbol of Cryto to be converted
        :param eSymbol: The symbol of Cryto convert to
        """
        self.symbol = symbol
        self.eSymbol = eSymbol
   
    def getOrderBook(self,startDate, endDate, interval):
        """
        Get Order Book
        :param startDate: The start Unix Timestamp
        :param endDate: The end Unix Timestamp
        :param interval: Frequency of requesting data
        """
        endPoint = END_POINT + "/api/v3/klines"
        url = endPoint + "?symbol=" + self.symbol + self.eSymbol + "&" +"interval=" + interval +"&startTime=" + startDate +"&endTime=" + endDate
        
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.text
        

        