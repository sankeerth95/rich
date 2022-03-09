import yfinance as yf
import matplotlib.pyplot as plt

def get_timed_tickers(start_time, end_time, symbols,\
     interval='1d'):
    plot_struct = {}
    for symb in symbols:
        ticker = yf.Ticker(symb)
        x = {}
        x['dividends'] = ticker.dividends[start_time:end_time]
        x['splits'] = ticker.splits[start_time:end_time]
        x['series'] = yf.download(symb, start=start_time, interval=interval, end=end_time)
        plot_struct[symb] = x
    return plot_struct


