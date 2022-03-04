from data.yfinance_data import get_timed_tickers



def fill_axes(ax, symbs, start_date, end_date):

    l = []
    l_dividend = []
    for k,v in get_timed_tickers(start_date, end_date, symbs).items():
        plot_series, = ax.plot(v['series']['High']/v['series']['High'][0], label=k)
        plot_dividend = ax.bar(v['dividends'].index, v['dividends'].values, width=4.0)
        l.append(plot_series)
        l_dividend.append(plot_dividend)

    ax.legend(l, symbs)
