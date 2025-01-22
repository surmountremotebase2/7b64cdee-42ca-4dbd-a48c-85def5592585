from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI, EMA, SMA, MACD, MFI, BB
from surmount.logging import log
from surmount.data import Asset, InstitutionalOwnership, InsiderTrading
from datetime import datetime

class TradingStrategy(Strategy):

   def __init__(self):
      self.tickers = ["RLJ", "UONE", "BYFC", "AXSM", "CARV", "AMS"]
      self.count = 0

   @property
   def interval(self):
      return "1day"

   @property
   def assets(self):
      return self.tickers

   def run(self, data):
      today = datetime.strptime(str(next(iter(data['ohlcv'][-1].values()))['date']), '%Y-%m-%d %H:%M:%S')
      yesterday = datetime.strptime(str(next(iter(data['ohlcv'][-2].values()))['date']), '%Y-%m-%d %H:%M:%S')
      
      if today.day == 14 or (today.day > 14 and yesterday.day < 14):
          return TargetAllocation({k: 1/len(self.tickers) for k in self.tickers})
      return None
