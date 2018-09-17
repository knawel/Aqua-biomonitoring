from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/fig')
def fig():
    fig, ax = plt.subplots()
    Ntotal = 1000
    N, bins, patches = ax.hist(np.random.rand(Ntotal), 20)

    fracs = N.astype(float)/N.max()
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = cm.jet(norm(thisfrac))
        thispatch.set_facecolor(color)

    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')