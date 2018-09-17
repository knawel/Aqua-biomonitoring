from app import app
from flask import render_template
import mpld3
import numpy as np

import matplotlib as plt

import random


x = range(100)
y = [a * 2 + random.randint(-20, 20) for a in x]

def draw_fig(fig_type):
    """Returns html equivalent of matplotlib figure
    Parameters
    ----------
    fig_type: string, type of figure
            one of following:
                    * line
                    * bar
    Returns
    --------
    d3 representation of figure
    """

    fig, ax = plt.subplots()
    if fig_type == "line":
        ax.plot(x, y)
    elif fig_type == "bar":
        ax.bar(x, y)
    elif fig_type == "scatter":
        ax.scatter(x, y)
    elif fig_type == "hist":
        ax.hist(y, 10, normed=1)
    elif fig_type == "area":
        ax.plot(x, y)
        ax.fill_between(x, 0, y, alpha=0.2)

    return mpld3.fig_to_html(fig)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/fig')
def fig():
    return draw_fig(data["line"])


# if __name__ == '__main__':
#     app.debug = True
#     app.run()