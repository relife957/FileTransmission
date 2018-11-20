import requests
from prettyprinter import pprint
import other_api.api_keys as api_keys

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


def poem():
    url = "https://api.apiopen.top/singlePoetry"
    res = get_data(url)
    return res


def get_players_list():
    url = "https://api.opendota.com/api/proPlayers"
    params = {
        'api_key': "B6F03F91CD8355AD6856E6DF03854370",
    }
    match_list = get_data(url, params)
    res_list = []
    for match in match_list:
        if type(match) == dict:
            try:
                res_list.append(match['account_id'])
            except:
                continue
    return res_list

def get_player_detail(account_id):
    url = "https://api.opendota.com/api/players/{0}".format(account_id)
    params = {
        'api_key': "B6F03F91CD8355AD6856E6DF03854370",
    }
    player_data = get_data(url,params)
    return player_data

def main():
    poem()


if __name__ == '__main__':
    main()