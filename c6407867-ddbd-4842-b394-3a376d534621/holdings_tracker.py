from datetime import datetime

possible_tickers = [
    "AAPL",
    "V",
    "MSFT",
    "UNH",
    "TMUS",
    "CB",
    "GOOG",
    "MOH",
    "JPM",
    "HD",
    "SCHW",
    "TSLA",
    "TMO",
    "MMC",
    "DHR",
    "ACN",
    "DG"
]

holdings = {
    "2022-07-31": {
        "MSFT": .157,
        "AAPL": .111,
        "UNH": .088,
        "DHR": .076,
        "ACN": .057,
        "V": .057,
        "TMO": .057,
        "MMC": .054,
        "CB": .055,
        "DG": .055
    },
    "2023-01-31": {
        "MSFT": .127,
        "AAPL": .092,
        "UNH": .074,
        "V": .059,
        "CB": .055,
        "MMC": .054,
        "JPM": .053,
        "DHR": .053,
        "TMO": .053,
        "ACN": .053
    }
}

def get_holdings(date):
    return holdings.get(date, None)
