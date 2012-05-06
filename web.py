import flask
app = flask.Flask(__name__)

from pywiki import wiki

@app.route("/")
def index():
    return flask.redirect(flask.url_for('show', page='Main Page'))

@app.route("/wiki/<page>")
def show(page):
    return wiki.render_page(page)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

