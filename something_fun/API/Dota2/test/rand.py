# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     rand
   Description :
   Author :       wangyi
   date：          11/24/18
-------------------------------------------------
   Change Activity:
                   11/24/18:
-------------------------------------------------
"""
__author__ = 'wangyi'
from API.Dota2.config.api_keys import openDota_param

def one():
    a = openDota_param
    a['1'] = '2'
    print(a)

def two():
    openDota_param['2'] = '3'
    print(openDota_param)


if __name__ == '__main__':
    with open('data.dat','w') as f:
        f.write(str((1,2)))
        f.write('\n')
        f.write(str((2,3))[1:-1])