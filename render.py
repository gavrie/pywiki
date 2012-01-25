import re

def wiki2html(text):
    out_lines = []
    for line in text.splitlines():
        if line.strip() == '':
            out_lines.append("<p>")
        line = re.sub(r"\[([^]]+)\]", r'<a href="\1">\1</a>', line)
        out_lines.append(line)
    return "\n".join(out_lines)

def edit2html(text):
    html = """
    <form method="POST">
    <textarea name="contents" rows="20" cols="80">{text}</textarea>
    <input type="submit" value="Save"/>
    <input type="reset" value="Reset"/>
    </form>
    """.format(text=text)
    return html

def render_page(title, contents, edit=False):
    if not edit:
        body = wiki2html(contents)
    else:
        body = edit2html(contents)
    header = """
        <h1>Our Nice Wiki</h1>
        <h2>{title}</h2>
        <hr>
    """.format(title=title)
    footer = """
        <p>
        <hr>
        <p><a href="/wiki/Main Page">Main Page</a> | <a href="/edit/{title}">Edit this page</a></p>
    """.format(title=title)
    page = header + body + footer
    return page
