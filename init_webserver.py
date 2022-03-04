import io
from flask import Flask, Response
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from data.symbs import faang, equity_listing_reuters_ric

from visualize.chart_utils import fill_axes


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    symbs = [ equity_listing_reuters_ric[symb] for symb in faang ]
    fill_axes(axis, symbs, '2021-01-01', '2022-03-02')
    return fig


app = Flask('screener')

@app.route('/')
def hello():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)

