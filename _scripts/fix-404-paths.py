"""Post-render: clean up root-relative links in docs/404.html.

On Windows, Quarto writes the 404 page's site-absolute links as "/.\\path" (for
example "/.\\assets/Logos/x.svg"). Browsers normalise these to "/path", but the
output is fragile and ugly, so rewrite them to plain "/path".
"""
import pathlib
import re

page = pathlib.Path("docs/404.html")
if page.exists():
    html = page.read_text(encoding="utf-8")
    fixed = re.sub(r'(["\'])/\.(?:\\|/)', r"\1/", html)       # "/.\path" -> "/path"
    fixed = fixed.replace("/." + "\\", "/")                     # "https://kai.do/.\path" too
    if fixed != html:
        page.write_text(fixed, encoding="utf-8")
