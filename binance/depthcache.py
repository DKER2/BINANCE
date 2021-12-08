import requests
class DepthCache: 
    def __init__(self, symbol,eSymbol,startDate, endDate, frequency):
        self.symbol = symbol
        self.eSymbol = eSymbol
        self.startDate = startDate
        self.endDate = endDate
        self.frequency = frequency
    def getOrderBook():
        
        