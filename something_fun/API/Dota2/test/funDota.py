import sys
sys.path.append(r"/home/wangyi/PycharmProjects/something_fun")
from API.fundata.client import *
from API.Dota2.config import api_keys
from prettyprinter import pprint

"""
fundota接口的测试使用
"""
def request(param):
    keys = api_keys.keys['funDota']
    init_api_client(keys['API_KEY'], keys['API_SECRET'])

    client = get_api_client()
    uri = "/data-service/dota2/public/match/{0}/players_ability_upgrades".format(param)
    data = {}
    res = client.api(uri, data)
    return res



def main():
    res = request("4234965007")
    pprint(res)

if __name__ == '__main__':
    main()



