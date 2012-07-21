import flask
app = flask.Flask(__name__)

FOOTER = """
<hr>
<p>
<a href="/show/Main">Main</a>
<a href="/show/Second">Second</a>
"""

BODY = """
This is the "{page}" page. 
<p>
<a href="/edit/{page}">Edit this page</a>
"""

EDIT_BODY = """
This is the "{page}" page in editing mode:
<form method="POST">
    <textarea name="contents" rows="20" cols="80"></textarea>
    <p>
    <input type="submit" value="Submit"/>
</form>
"""

POSTED_BODY = """
These contents were posted:
<p>
<pre>
{posted_data}
</pre>
"""

@app.route("/")
def index():
    return flask.redirect(flask.url_for('show', page='Main'))

@app.route("/show/<page>")
def show(page):
    contents = BODY + FOOTER
    return contents.format(page=page)

@app.route("/edit/<page>", methods=["GET", "POST"])
def edit(page):
    if flask.request.method == "POST":
        posted_data = dict(flask.request.form)
        contents = POSTED_BODY + FOOTER
        return contents.format(page=page, posted_data=posted_data)
    else:
        contents = EDIT_BODY + FOOTER
        return contents.format(page=page)

if __name__ == "__main__":
    app.secret_key = "foobar"
    app.run(host='localhost', port=5000, debug=True)
