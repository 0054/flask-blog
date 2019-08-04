import markdown

def markdown_renderer(text):
    html_post = markdown.markdown(text, extensions=['codehilite'])
    return html_post
