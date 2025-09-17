# pipeline.py
import yfinance as yf
import datetime
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DB_FILE = os.getenv("DB_FILE", "market_data.csv")


def run_ingest(tickers: list[str]):
    if tickers is None:
        tickers = ["AAPL", "MSFT"]
    print("tickerz", tickers)
    today = datetime.date.today()
    start = today - datetime.timedelta(days=30)  # fetch last 30 days

    try:
        df = yf.download(tickers, start=start, end=today)["Close"]
    except Exception as e:
        print(f"Download failed: {e}")
        return

    if df.empty:
        print("No data downloaded - yfinance may be having issues")
        return

    df = df.reset_index()
    df.to_csv(DB_FILE, index=False)
    print(f"Ingested {len(df)} rows into {DB_FILE}")


def get_data():
    try:
        return pd.read_csv(DB_FILE)
    except FileNotFoundError:
        print("No DB file found. Run /ingest first.")
        return pd.DataFrame()
