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
    WIKI_LINK_RE   = r"""
        \[              # Literal '['
            (           # Start group
              [^]]+     # Any character except ']', one or more times
            )           # End group
        \]              # Literal ']'
    """
    WIKI_LINK_HTML = r'<a href="\1">\1</a>'

    out_lines = []
    for line in text.splitlines():
        if line.strip() == '':
            out_lines.append("<p>")
        line = re.sub(WIKI_LINK_RE, WIKI_LINK_HTML, line, flags=re.VERBOSE)
        out_lines.append(line)
    return "\n".join(out_lines)


def render_page(title, contents):
    header = TEMPLATE_HEADER.format(title=title)
    footer = TEMPLATE_FOOTER.format(title=title)

    body = wiki2html(contents)

    page = SEPARATOR.join([header, body, footer])
    return page
