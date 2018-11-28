from datetime import datetime
import API.ydcv
import json
from prettyprinter import cpprint,set_default_style
import requests

"""
测试翻译(已弃用)
"""

def time_tansform(time_str):
    return datetime.fromtimestamp(time_str).strftime("%Y-%m-%d %H:%M:%S")


def translation():
    ydcv = API.ydcv
    word = 'Bloodseeker'
    data = json.loads(ydcv.lookup_word(word))
    value = data['web']
    for dic in value :
        if dic['key'].upper()  ==word.upper():
            print(dic['value'][0])
        else :
            print(word,dic['key'])


def loadJson():
    dicts = {}
    with open('./Dota2/英雄对应.json','r') as f:
        dicts = json.load(f)
    # pprint(dicts)
    return dicts



def get():
    url = "https://api.opendota.com/api/explorer"
    param = {
        'api_key': "B6F03F91CD8355AD6856E6DF03854370",
        'sql': 'select match_id from match_patch limit 10'
    }
    res = requests.get(url,param)
    return res.json()



def main():
    set_default_style('light')
    cpprint(time_tansform(1540798607))



if __name__ == '__main__':
    main()