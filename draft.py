import requests
import json


def translator():
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20170509T173115Z.7389ba585fa6cfbd.673ddf47a800eab1bf15efb75ffdc3db68bcba5f'

    text = "привет"

    r = requests.post(url, data={'key': key, 'text': text, 'lang': 'ru-en'})
    word_translation =  r.json()['text'][0]
    print(word_translation)

translator()