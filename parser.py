import urllib.request
from bs4 import BeautifulSoup


def user_site():
    site = str(input('Example: https://docs.python.org/3.0/library/urllib.request.html \nEnter web site to parse:'))
    return site


def get_html():
    try:
        url = user_site()
        reply = urllib.request.urlopen(url)
        return reply.read()
    except urllib.error.HTTPError:
        print('Forbidden, try another site')


def parser_html(html=get_html()):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()
    except TypeError:
        return('bad luck')


print(parser_html())