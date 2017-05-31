import requests
import urllib.request
from bs4 import BeautifulSoup

web_site = input('Example: http://docs.python-requests.org/en/master/ \nEnter your site: ')


class Parser:

    def __init__(self, site):
        self.site = site

    def get_text(self):
        try:
            reply = urllib.request.urlopen(self.site)  # open url
            soup = BeautifulSoup(reply.read(), 'html.parser')  # format html
            return soup.get_text()  # get text from html
        except urllib.error.HTTPError:
            return 'Forbidden, try another site'
        except ValueError as err:
            return err


class YandexTrans(Parser):

    def __init__(self, text='Hello', lang='en-ru', url='https://translate.yandex.net/api/v1.5/tr.json/translate?',
                 key='trnsl.1.1.20170509T173115Z.7389ba585fa6cfbd.673ddf47a800eab1bf15efb75ffdc3db68bcba5f'):
        self.lang = lang
        self.text = text
        self.url = url
        self.key = key

    def get_rqst(self):
        a = Parser(web_site)
        r = requests.get(self.url, data={'key': self.key, 'text': a.get_text(), 'lang': self.lang})
        return r.json()['text'][0]


translate_site = YandexTrans()

if __name__ == '__main__':
    print(translate_site.get_rqst())
