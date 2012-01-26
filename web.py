import flask
app = flask.Flask(__name__)

from pywiki import wiki

@app.route("/")
def index():
    return flask.redirect(flask.url_for('show', page='Main Page'))

@app.route("/wiki/<page>")
def show(page):
    return wiki.render_page(page)

@app.route("/edit/<page>", methods=["GET", "POST"])
def edit(page):
    if flask.request.method == "POST":
        wiki.update_page(page, flask.request.form['contents'])
        return flask.redirect(flask.url_for('show', page=page))
    else:
        return wiki.render_page_edit(page)

@app.route("/contents")
def contents():
    return wiki.render_toc()

if __name__ == "__main__":
    app.secret_key = "foobar"
    app.run(host='0.0.0.0', port=5000, debug=True)

