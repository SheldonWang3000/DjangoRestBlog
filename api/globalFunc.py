import re
import markdown2
from bs4 import BeautifulSoup

def markdown2Text(markdownText):
    """ Converts a markdown string to plaintext """

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown2.markdown(markdownText)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)
    html = re.sub(r'\n', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))
    text = re.sub(r' +', ' ', text)

    return text

def markdown2Abstract(markdownText):
    fullText = markdown2Text(markdownText)
    l = 200
    if len(fullText) > l:
        abstract = fullText[:fullText.find(' ', l)] + '...'
    else:
        abstract = fullText
    return abstract
