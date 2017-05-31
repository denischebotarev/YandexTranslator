import requests


class YandexTrans:

    def __init__(self, text='Hello', lang='en-ru', url='https://translate.yandex.net/api/v1.5/tr.json/translate?',
                 key='trnsl.1.1.20170509T173115Z.7389ba585fa6cfbd.673ddf47a800eab1bf15efb75ffdc3db68bcba5f'):
        self.lang = lang
        self.text = text
        self.url = url
        self.key = key

    def rqst(self):
        r = requests.get(self.url, data={'key': self.key, 'text': self.text, 'lang': self.lang})
        return r.json()['text'][0]


first = YandexTrans(input('Enter your text: '), input('Enter languages (example en-ru): '))
if __name__ == '__main__':
    print(first.rqst())

