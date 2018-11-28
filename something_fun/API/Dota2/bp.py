#!/usr/bin/env python
# -*- coding: utf-8 -*-

from API.fundata.client import *
from API.Dota2.config import api_keys
import requests

"""
抓取一万条比赛bp,存入bp.dat
"""

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


def get_bp(matchid_win):
    keys = api_keys.keys['funDota']
    init_api_client(keys['API_KEY'], keys['API_SECRET'])

    client = get_api_client()
    uri = "/data-service/dota2/public/match/{0}/ban_picks".format(matchid_win[0])
    temp = {}
    res = client.api(uri, temp)
    result = []
    try:
        data = res['data']
        for bp_dict in data:
            hero_id = crawl_team(bp_dict,matchid_win[1])
            if hero_id is not None:
                result.append(hero_id)
    except:
        return len(result)
    if len(result) == 5:
        return result
    return len(result)


def crawl_team(bp_dict,flag):
    team_num = 0 if flag else 1
    if bp_dict['is_pick'] and bp_dict['team']==team_num:
        return bp_dict['hero_id']


def get_match_list(less_match_id):
    url = "https://api.opendota.com/api/proMatches"
    params = {
        'api_key': api_keys.keys["openDota"],
        'less_than_match_id':less_match_id
    }
    match_list = get_data(url,params)
    res_list = []
    for match in match_list:
        if type(match)==dict:
            try:
                temp_dict = (match['match_id'],match['radiant_win'])
                res_list.append(temp_dict)
            except:
                continue
    return res_list

def find_min_match_id(match_list):
    min_num = match_list[0][0]
    for tuples in match_list:
        if tuples[0] < min_num:
            min_num = tuples[0]
    return min_num

def main():
    max_num = 4197659256
    f = open('./data/bp.dat','w')
    for i in range(100):
        match_list = get_match_list(max_num)
        for match in match_list:
            bp_team = str(get_bp(match))
            f.write(bp_team+'\n')
        max_num = find_min_match_id(match_list)
    f.close()
if __name__ == '__main__':
    main()