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
{content}
<p>
<a href="/edit/{page}">Edit this page</a>
"""

EDIT_BODY = """
This is the "{page}" page in editing mode:
<form method="POST">
    <textarea name="contents" rows="20" cols="80">{content}</textarea>
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

pages = {}

@app.route("/")
def index():
    return flask.redirect(flask.url_for('show', page='Main'))

@app.route("/show/<page>")
def show(page):
    contents = BODY + FOOTER
    return contents.format(page=page, content=pages.get(page, ""))

@app.route("/edit/<page>", methods=["GET", "POST"])
def edit(page):
    if flask.request.method == "POST":
        text = flask.request.form['contents']
        pages[page] = text
        print pages
        contents = POSTED_BODY + FOOTER
        return flask.redirect(flask.url_for('show', page=page))
        #return contents.format(page=page, posted_data=text)
    else:
        contents = EDIT_BODY + FOOTER
        return contents.format(page=page, content=pages.get(page, ""))

if __name__ == "__main__":
    app.secret_key = "foobar"
    app.run(host='localhost', port=5000, debug=True)
