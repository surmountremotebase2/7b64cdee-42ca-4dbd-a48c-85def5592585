
from surmount.base_class import Strategy, TargetAllocation
from surmount.logging import log
from surmount.data import Asset, Correlation

class TradingStrategy(Strategy):

   def __init__(self):
      self.tickers = ["GLD", "USO"]
      self.data_list = [Correlation("GLD", "USO")]

   @property
   def interval(self):
      return "1day"

   @property
   def assets(self):
      return self.tickers

   @property
   def data(self):
      return self.data_list

   def run(self, data):
      corr = data[("correlation", "GLD", "USO")]
      if corr is None or len(corr) == 0:
          return TargetAllocation({})

      gld_stake = 0
      uso_stake = 0

      if corr[-1] > 0.5:
         gld_stake = 0.5
         uso_stake = 0.5
      elif corr[-1] < -0.5:
         gld_stake = -0.5
         uso_stake = -0.5
      else:
         gld_stake = 0
         uso_stake = 0

      return TargetAllocation({"GLD": gld_stake, "USO": uso_stake})