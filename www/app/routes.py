from app import app
from flask import render_template
import matplotlib.pyplot as plt
import io
import base64



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/fig')
def fig():

    img = io.BytesIO()

    y = [1, 2, 3, 4, 5]
    x = [0, 2, 1, 3, 4]
    plt.plot(x, y)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('fig.html', plot_url='<img src="data:image/png;base64,{}">')

if __name__ == '__main__':
    app.debug = True
    app.run()