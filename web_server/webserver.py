import io, os
from lib2to3.pgen2.literals import simple_escapes
from flask import Flask

from visualize.chart_utils import sample_chart
from flask import Response
from flask import render_template



def create_app(test_config=None):
    # create and configure the app
    app = Flask('web_server', instance_relative_config=True)


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

