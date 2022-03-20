import flask
from flask import Flask
from visualize.chart_utils import sample_chart

from flask import render_template, jsonify
from flask.helpers import get_root_path

import web_server.datarequest_handler as  drh

from datetime import datetime

from data.yfinance_data import get_timed_tickers, get_series_data_high



def create_app(test_config=None):
    # create and configure the app
    app = Flask('web_server', instance_relative_config=True)


    @app.route('/callback', methods=["GET", "POST"])
    def callback():
        graphJSON = drh.gm(flask.request.args.get('data'))
        return graphJSON


    @app.route('/graphs_control', methods=["POST"])
    def graphs_control():
        datajson = flask.request.json

        if datajson['button_id'] == 'draw_graph':
            ric = datajson['RIC']
            start_date = datetime.strptime(datajson['start_date'], "%Y-%m-%d")
            end_date = datetime.strptime(datajson['end_date'], "%Y-%m-%d")
            interval = datajson['interval']

            symbols = [ ric ]
            print(start_date, end_date, ric)
            ps = get_timed_tickers(start_date, end_date, symbols, interval=interval)
            series = get_series_data_high(ps)[0]
            xvals = [ datetime.strftime(dt, '%Y-%m-%d') for dt in series.index ]
            yvals = series.values.tolist()
            return jsonify({'x': xvals, 'y': yvals})
        else:
            return ''


    @app.route('/button_handler_base')
    def button_handler_base():
 
        aid = flask.request.args.get('button_id')
        if aid == "graph_screener":
            return render_template('graph_screen.html')
        else:
            return "UNIMPLEMENTED REQUEST"


    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('base.html')


    return app


if __name__ == '__main__':
    create_app.run(host='localhost', port=8000, debug=True)

