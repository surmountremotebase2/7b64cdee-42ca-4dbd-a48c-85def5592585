from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI, EMA, SMA, MACD, MFI, BB, ATR
from surmount.logging import log

class TradingStrategy(Strategy):

   @property
   def assets(self):
      return ["TQQQ", "SPY", "UVXY"]

   @property
   def interval(self):
      return "1hour"

   def run(self, data):
      spy_stake = 0
      d = data["ohlcv"]
      atr = ATR("TQQQ", d, 40)
      qqq_stake = 0
      if len(d)>3 and "13:00" in d[-1]["TQQQ"]["date"] and atr[-1]/d[-1]["TQQQ"]["close"]>0.001:
         v_shape = d[-2]["TQQQ"]["close"]<d[-3]["TQQQ"]["close"] and d[-1]["TQQQ"]["close"]>d[-2]["TQQQ"]["close"]
         log(str(v_shape))
         if v_shape:
            qqq_stake = 1 - 0.005
         else: spy_stake = 0.5 - 0.005
      elif len(d)>3:
         spy_stake = 0.5 - 0.005

      return TargetAllocation({"TQQQ": qqq_stake, "SPY": spy_stake, "UVXY": 0.005})
