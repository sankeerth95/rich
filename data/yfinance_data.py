import yfinance as yf
import matplotlib.pyplot as plt

def plot_timed_tickers(start_time, end_time, symbols, interval='1d', normalize=True):

    plot_struct = {}
    for symb in symbols:
        ticker = yf.Ticker(symb)
        x = {}
        x['dividends'] = ticker.dividends[start_time:end_time]
        x['splits'] = ticker.splits[start_time:end_time]
        x['series'] = yf.download(symb, start=start_time, interval=interval, end=end_time)
        plot_struct[symb] = x
    

    return plot_struct

def fill_axes(ax, symbs, start_date, end_date):
    l = []
    l_dividend = []
    for k,v in plot_timed_tickers(start_date, end_date, symbs).items():
        plot_series, = ax.plot(v['series']['High']/v['series']['High'][0], label=k)
        plot_dividend = ax.bar(v['dividends'].index, v['dividends'].values, width=4.0)
        l.append(plot_series)
        l_dividend.append(plot_dividend)

    ax.legend(l, symbs)


for __name__ == '__main__':
    symbs = [
    'msft',
    'aapl',
    'goog',
    'amzn',
    ]
    fig, axes = plt.subplots(2, 1)
    fill_axes(axes[0], symbs, '2020-01-01', '2021-01-01')
    fill_axes(axes[1], symbs, '2020-01-01', '2021-01-01')

    plt.show()

