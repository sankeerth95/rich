import flask
from flask import Flask
from visualize.chart_utils import sample_chart
from flask import Response
from flask import render_template, jsonify
from flask.helpers import get_root_path

from dash import Dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc
import dash_table

from datetime import datetime

from data.yfinance_data import get_timed_tickers, get_series_data_high



import numpy as np
import pandas as pd

"""Plotly Dash HTML layout override."""

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/logo.png" class="logo" />
                    <h1>Plotly Dash Flask Tutorial</h1>
                  </a>
                <nav>
                </nav>
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv("311-calls.csv", parse_dates=["created"])
    df["created"] = df["created"].dt.date
    df.drop(columns=["incident_zip"], inplace=True)
    num_complaints = df["complaint_type"].value_counts()
    to_remove = num_complaints[num_complaints <= 30].index
    df.replace(to_remove, np.nan, inplace=True)
    return df


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table



def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["complaint_type"],
                            "text": df["complaint_type"],
                            "customdata": df["key"],
                            "name": "311 Calls by region.",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "NYC 311 Calls category.",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_app.server



def create_app(test_config=None):
    # create and configure the app
    app = Flask('web_server', instance_relative_config=True)



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
            return render_template('panel/graph_screen.html')
        else:
            return "UNIMPLEMENTED REQUEST"


    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('base.html')


    app = init_dashboard(app)
    return app







def register_dashapps(app):
    from dashutils.layout import layout
    from dashutils.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp = Dash(__name__,
                    server=app,
                    url_base_pathname='/dashboard/',
                    assets_folder=get_root_path(__name__) + '/dashboard/assets/',
                    meta_tags=[meta_viewport])

    with app.app_context():
        dashapp.title = 'Dashapp'
        dashapp.layout = layout
        register_callbacks(dashapp)












if __name__ == '__main__':
    create_app.run(host='localhost', port=8000, debug=True)

