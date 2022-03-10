import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def get_timed_tickers(start_time: datetime, end_time: datetime, symbols,\
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

def get_series_data_high(plot_struct):
    l = []
    for k,v in plot_struct.items():
        l.append( v['series']['High'] )

    return l

def get_series_data_low(plot_struct):
    l = []
    for k,v in plot_struct.items():
        l.append( v['series']['Low'] )

    return l



if __name__ == '__main__':

    sd = datetime.strptime('2021-01-01', '%Y-%m-%d')
    ed = datetime.strptime('2022-01-01', '%Y-%m-%d')
    ps = get_timed_tickers(sd, ed, ['msft'])
    x = get_series_data_high(ps)
    print(x)