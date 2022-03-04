from data.yfinance_data import get_timed_tickers
from matplotlib.figure import Figure
from data.symbs import faang, equity_listing_reuters_ric
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg

def fill_axes(ax, symbs, start_date, end_date):

    l = []
    l_dividend = []
    for k,v in get_timed_tickers(start_date, end_date, symbs).items():
        plot_series, = ax.plot(v['series']['High']/v['series']['High'][0], label=k)
        plot_dividend = ax.bar(v['dividends'].index, v['dividends'].values, width=4.0)
        l.append(plot_series)
        l_dividend.append(plot_dividend)

    ax.legend(l, symbs)



def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    symbs = [ equity_listing_reuters_ric[symb] for symb in faang ]
    fill_axes(axis, symbs, '2021-01-01', '2022-03-02')
    return fig



def sample_chart():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return output.getvalue()

