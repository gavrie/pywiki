import re

TEMPLATE_HEADER = """
    <h1>Our Nice Wiki</h1>
    <h2>{title}</h2>
    <hr>
    """

TEMPLATE_FOOTER = """
    <p>
    <hr>
    <p><a href="/wiki/Main Page">Main Page</a> | <a href="/edit/{title}">Edit this page</a></p>
    """

SEPARATOR = ""

def wiki2html(text):
    out_lines = []
    for line in text.splitlines():
        if line.strip() == '':
            out_lines.append("<p>")
        line = re.sub(r"\[([^]]+)\]", r'<a href="\1">\1</a>', line)
        out_lines.append(line)
    return "\n".join(out_lines)


def render_page(title, contents):
    header = TEMPLATE_HEADER.format(title=title)
    footer = TEMPLATE_FOOTER.format(title=title)

    body = wiki2html(contents)

    page = SEPARATOR.join([header, body, footer])
    return page
