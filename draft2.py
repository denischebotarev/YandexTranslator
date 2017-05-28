import requests
import urllib.request
from bs4 import BeautifulSoup


def get_html(url='http://englishstory.ru/from-the-history-of-a-letter-2.html'):
    reply = urllib.request.urlopen(url)
    return reply.read()


def parser_html(html=get_html()):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()


def translator():
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20170509T173115Z.7389ba585fa6cfbd.673ddf47a800eab1bf15efb75ffdc3db68bcba5f'
    lang = str(input('Enter language (Example: ru-en): '))
    text = str(parser_html())
    # print(text)

    r = requests.get(url, data={'key': key, 'text': text, 'lang': lang})
    word_translation = r.json()['text'][0]
    print(word_translation)

translator()