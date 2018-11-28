# -*- coding: utf-8 -*-
import os
import sys
from pprint import pprint
from API.fundata.request import ApiClient
from API.fundata.client import init_api_client
from API.fundata.dota2.match import get_batch_basic_info
import API.Dota2.config.api_keys
"""
测试fundota接口

"""

print(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def test():
    # FIXME，需要设置 public_key/secret_key
    public_key, secret_key = ('', '')

    # 用 public key，secret key 来初始化 client
    client = ApiClient(public_key, secret_key)

    # 准备 API 需要的参数
    uri = '/data-service/dota2/public/match/{0}/basic_info'.format(3765833999)
    data = {}

    res = client.api(uri, data)

    pprint(res)


# 测试获取批量比赛基本数据
def test_batch_basic_info():
    keys = API.Dota2.config.api_keys.keys
    # FIXME，需要设置 public_key/secret_key
    init_api_client(api_secret=keys['funDota']['API_SECRET'],
                    public_key=keys['funDota']['API_KEY'])

    res = get_batch_basic_info(1522724457, 0, 2)
    pprint(res)


if __name__ == "__main__":
    test_batch_basic_info()
