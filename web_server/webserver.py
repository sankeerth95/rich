import flask
from flask import Flask

from visualize.chart_utils import sample_chart
from flask import Response
from flask import render_template



def create_app(test_config=None):
    # create and configure the app
    app = Flask('web_server', instance_relative_config=True)


    @app.route('/graphs_control', methods=["POST"])
    def graphs_control():
        datajson = flask.request.json
        print(datajson)
        return "adg"


    @app.route('/button_handler_base')
    def button_handler_base():
 
        aid = flask.request.args.get('button_id')
        if aid == "graph_screener":
            return render_template('panel/graph_screen.html')
        else:
            return "UNIMPLEMENTED REQUEST"





    @app.route('/plot.png')
    def plot_png():
        return Response(sample_chart(), mimetype='image/png')


    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('base.html')



    return app

if __name__ == '__main__':
    create_app.run(host='localhost', port=8000, debug=True)

