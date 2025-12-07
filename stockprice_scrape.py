

import yfinance as yf
import pandas as pd
from google.colab import files  

# Stock symbols for rddt
TARGET_TICKERS = [
    "AAOI", "AAPL", "ABXX", "ACHR", "ADBE", "ALLY", "AMBA", "AMD", "AMPX", "AMZN", 
    "ANF", "APLD", "ASPI", "AVGO", "BE", "BEAM", "BMNR", "BROS", "BULL", "CA", 
    "CDTX", "CIFR", "CMCSA", "CRSR", "CRWV", "DASH", "DKNG", "DLTR", "DND", "DNUT", 
    "DUOL", "ENPH", "ES", "ET", "FLNC", "GAP", "GDX", "GLD", "GME", "GO", 
    "GOOG", "GOOGL", "GRAB", "GRND", "GTBIF", "HIMS", "HOG", "HOOD", "HTZ", "IHRT", 
    "INTC", "IREN", "JOBY", "LABU", "LDI", "LUMN", "LUNR", "MATH", "META", "MSFT", 
    "MSTR", "MSTY", "MU", "NBIS", "NEM", "NFLX", "NICE", "NUAI", "NVDA", "OPEN", 
    "PACS", "PFE", "PGY", "PLTR", "PM", "POET", "PSKY", "PYPL", "QBTS", "QCOM", 
    "QQQ", "RDDT", "RDW", "RGTI", "RIVN", "RKLB", "RKT", "SBUX", "SEZL", "SFTBY", 
    "SG", "SNAP", "SOFI", "SOUN", "SPT", "^GSPC", "SPXL", "SPY", "SQQQ", "TE", 
    "TOST", "TQQQ", "TSLA", "TTWO", "UUUU", "VOYG", "VXX", "WEN", "WULF"
]

OUTPUT_FILENAME = "november_stock_data.csv"
START_DATE = "2025-11-01"
END_DATE = "2025-12-01"

def smart_fetch(ticker):
   #US Stock market first, if not then Canada
    stock = yf.Ticker(ticker)
    hist = stock.history(start=START_DATE, end=END_DATE)
    if not hist.empty:
        return hist, ticker
    suffixes = [".TO", ".NE", ".V"]
    for suffix in suffixes:
        alt_ticker = ticker + suffix
        stock = yf.Ticker(alt_ticker)
        hist = stock.history(start=START_DATE, end=END_DATE)
        if not hist.empty:
            return hist, alt_ticker
            
    return None, None

def main():
    data_buffer = []

    # Remove duplicates 
    unique_tickers = list(set(TARGET_TICKERS))

    for ticker in unique_tickers:
        try:
            hist, actual_ticker = smart_fetch(ticker)
            
            if hist is not None and not hist.empty:
                for date, row in hist.iterrows():
                    data_buffer.append({
                        "Ticker": actual_ticker,
                        "Date": date.strftime('%Y-%m-%d'),
                        "Open": row['Open'],
                        "Close": row['Close']
                    })
        except Exception:
            continue

    if data_buffer:
        df = pd.DataFrame(data_buffer)
        df.to_csv(OUTPUT_FILENAME, index=False)
        print("Successfull")
        files.download(OUTPUT_FILENAME) 
    else:
        print("No data")

if __name__ == "__main__":
    main()