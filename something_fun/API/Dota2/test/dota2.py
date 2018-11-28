import requests
from API.Dota2.config import api_keys
from prettyprinter import pprint
"""
dota2官方接口的测试
"""

def steamID(steamId):
    baseNum = 61197960265728
    steamId = int(steamId[3:])
    return steamId-baseNum

def get_data(url,param=None,headers=None):
    """

    :param url:目标url
    :param param: 传入参数 默认none
    :param headers: 传入的头信息 默认none
    :return:
    """
    res = None
    try:
        res = requests.get(url=url,
                           params=param,
                           headers=headers)
    except:
        return "访问失败"
    if res.status_code == 200:
        return res.json()
    else:
        return "错误: "+ str(res.status_code)

def printData(data):
    if type(data)==list :
        for json in data :
            if type(json) == dict:
                for item in json.items():
                    print(item[0]+" : " + data(item[1]))
            else:
                print(json)
    elif type(data)==dict:
        for item in data.items():
            print(item[0]+" : " + str(item[1]) )

def main():
    url = "https://api.opendota.com/api/search"
    param = {
        "api_key":api_keys.keys["openDota"],
        "q":"Relife"
    }
    res = get_data(url,param)
    pprint(res)
if __name__ == '__main__':
    main()