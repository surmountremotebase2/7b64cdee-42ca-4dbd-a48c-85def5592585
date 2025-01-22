from surmount.base_class import Strategy, TargetAllocation
from surmount.logging import log
from surmount.data import Asset
from surmount.technical_indicators import BB

class TradingStrategy(Strategy):

    def __init__(self):
        self.tickers = ["TQQQ", "GLD"]

    @property
    def interval(self):
        return "1day"

    @property
    def assets(self):
        return self.tickers

    def run(self, data):

        gld_price = [i["TQQQ"]["close"] for i in data["ohlcv"]]
        uso_price = [i["GLD"]["close"] for i in data["ohlcv"]]
        if len(gld_price)<10 or len(uso_price)<10:
            return None
        ratio = [gld_price[i]/uso_price[i] for i in range(len(data["ohlcv"]))]
        avg_ratio = sum(ratio)/len(ratio)
        
        gld_stake = (gld_price[-1]/uso_price[-1])/avg_ratio * 0.5
        uso_stake = 1-gld_stake
        bbands = BB("TQQQ", data["ohlcv"], 20, 1.5)

        if gld_price[-1]<bbands["lower"][-1] or gld_price[-1]>bbands["upper"][-1] :
            gld_stake /= 2
        return TargetAllocation({"TQQQ": gld_stake, "GLD": uso_stake})
