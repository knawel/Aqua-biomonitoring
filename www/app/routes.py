from app import app
from flask import render_template
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64


def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/fig')
def fig():
    # These coordinates could be stored in DB
    x1 = [0, 1, 2, 3, 4]
    y1 = [10, 30, 40, 5, 50]
    x2 = [0, 1, 2, 3, 4]
    y2 = [50, 30, 20, 10, 50]
    x3 = [0, 1, 2, 3, 4]
    y3 = [0, 30, 10, 5, 30]

    graph1_url = build_graph(x1, y1);
    graph2_url = build_graph(x2, y2);
    graph3_url = build_graph(x3, y3);

    return render_template('graphs.html',
                           graph1=graph1_url,
                           graph2=graph2_url,
                           graph3=graph3_url)


# if __name__ == '__main__':
#     app.debug = True
#     app.run()