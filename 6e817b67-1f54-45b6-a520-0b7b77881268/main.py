from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import EMA
from surmount.logging import log

class TradingStrategy(Strategy):

   def __init__(self):
      self.ticker = "TSLA"
      self.alloc = {self.ticker:0}
      

   @property
   def assets(self):
      return [self.ticker]

   @property
   def interval(self):
      return "1day"

   def run(self, data):
      if len(data["ohlcv"]) == 0: return TargetAllocation(self.alloc)
      short_ema = EMA(self.ticker, data["ohlcv"], 10)
      long_ema = EMA(self.ticker, data["ohlcv"], 50)
      if not (short_ema and long_ema): return TargetAllocation(self.alloc)
      if short_ema[-1] > long_ema[-1]:
         self.alloc = {self.ticker:1}
         return TargetAllocation(self.alloc)
      elif short_ema[-1] < long_ema[-1]:
         self.alloc = {self.ticker:0}
         return TargetAllocation(self.alloc)
      return TargetAllocation(self.alloc)