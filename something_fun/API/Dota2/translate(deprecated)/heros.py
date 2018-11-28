import json
import API.ydcv
import requests
from pprint import pprint

"""
翻译英雄名字(已弃用)
"""

baseUrl ="https://api.opendota.com/api/heroes"

def translation(word):
    ydcv = API.ydcv
    data = {}
    try:
        data = json.loads(ydcv.lookup_word(word))
    except:
        print(word)
    if 'web' not in data:
        return "null"
    for dic in data['web']:
        if dic['key'].upper() == word.upper():
            return dic['value']
        else :
            return 'null'

def getData():
    param = {
        'api_key':"B6F03F91CD8355AD6856E6DF03854370"
    }
    res = requests.get(baseUrl,param)
    return res.json()

def do():
    result = {}
    data = getData()
    for hero in data:
        hero_name = hero["localized_name"]
        result[hero_name] = translation(hero_name)
    return result

def write(jsons,fileName):
    """
    将一个json写入一个json文件中
    :param jsons:需要写入的json
    :param fileName: json文件名
    :return:
    """
    with open(fileName,'w') as f:
        json.dump(jsons,f,ensure_ascii=False)

def main():
    # print(translation("Bloodseeker"))
    pprint(do())
if __name__ == '__main__':
    main()