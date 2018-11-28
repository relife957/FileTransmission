# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     purchase
   Description :
   Author :       wangyi
   date：          11/24/18
-------------------------------------------------
   Change Activity:
                   11/24/18:
-------------------------------------------------
"""
import time

__author__ = 'wangyi'

import requests
from API.Dota2.config import api_keys

hero_purchase = []

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



def get_purchase_data(match_data,radiant_win):
    """
    获取match比赛中的玩家购买信息
    :param match_data:比赛信息
    :param radiant_win:天辉是否胜利
    :return:
    """
    for player in match_data['players']:
        player_slot = player['player_slot']
        if radiant_win and player_slot < 5:
            hero_purchase.append(
                (player['hero_id'],str(player['purchase_log']))
            )
        elif not radiant_win and player_slot >4 :
            hero_purchase.append(
                (player['hero_id'],str(player['purchase_log']))
            )


def get_match_data(match_id):
    """
    :param match_id: 比赛id
    :return:
    """
    url = "https://api.opendota.com/api/matches/{0}".format(match_id)
    match_data = get_data(url,api_keys.openDota_param)
    if isinstance(match_data,str):
        print(match_data)
        return None
    return match_data

def get_match_list(less_match_id):
    """
    获得职业比赛比赛id和胜利方
    :param less_match_id:
    :return:
    """
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
    """
    寻找比赛列表中最小的比赛id
    :param match_list:
    :return:
    """
    min_num = match_list[0][0]
    for tuples in match_list:
        if tuples[0] < min_num:
            min_num = tuples[0]
    return min_num



def main():
    max_num = 4197659256

    # for i in range(100):
    match_list = get_match_list(max_num)
    for match in match_list:
        time.sleep(0.5)
        print(match[0])
        match_data = get_match_data(match[0])
        if match_data :
            get_purchase_data(match_data, match[1])
        # max_num = find_min_match_id(match_list)
    with open('./data/purchase.dat','w') as f :
        for h_p in hero_purchase:
            f.write(str(h_p)[1:-1])
            f.write('\n')

if __name__ == '__main__':
    main()