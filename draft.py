import requests
from parser import parser_html


def translator():
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20170509T173115Z.7389ba585fa6cfbd.673ddf47a800eab1bf15efb75ffdc3db68bcba5f'
    lang = str(input('Enter language (Example: ru-en): '))
    text = parser_html()
    # print(text)

    r = requests.get(url, data={'key': key, 'text': text, 'lang': lang})
    word_translation = r.json()['text'][0]
    print(word_translation)

translator()