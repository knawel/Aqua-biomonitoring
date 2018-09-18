from app import app
from flask import render_template
import matplotlib.pyplot as plt
import io
import base64
import sys
import datetime
import time
import numpy as np
import os


def plot_temp():
    img = io.BytesIO()

    l_file = os.path.join(os.path.join("app", "static"), 'light.log')
    light_data = []
    light_time = []
    with open(l_file, "r") as iFile:
        for i in iFile:
            j = i.strip().split('\t')
            time_ = j[0]
            light_ = j[1]
            light_data.append(light_)
            light_time.append(time.strptime(time_, "%Y-%m-%d %H:%M:%S.%f").tm_hour)
    light_time = np.array(light_time)
    light_data = np.array(light_data, dtype=float)
    plt.plot(light_time, light_data, '.')
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home')


@app.route('/fig')
def fig():
    plot_url = plot_temp()
    return render_template('fig.html', PL=plot_url, title = "Status")

# if __name__ == '__main__':
#     app.debug = True
#     app.run()