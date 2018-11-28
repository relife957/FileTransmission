# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     datetime_test
   Description :
   Author :       wangyi
   date：          11/22/18
-------------------------------------------------
   Change Activity:
                   11/22/18:
-------------------------------------------------
"""
import time

__author__ = 'wangyi'

from datetime import datetime

# 1:datetime类型 -> 格式化字符串
now = datetime.now()# time_str = now.strftime('%Y-%m-%d %H:%M:%S')


# 2:timestrap -> 格式化时间
t = time.time()    #<float>1542858847.261912
dataArray = datetime.utcfromtimestamp(t)  #<datetime>2018-11-22 03:54:17.388592
# time_str = now.strftime('%Y-%m-%d %H:%M:%S')   #<str>2018-11-22 11:55:01
# print(time_str)

# 3:格式化字符串 -> 时间戳
time_str = "2018-11-22 11:55:01"
datetimes = datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S') #<datetime> 2018-11-22 11:55:01
ts = datetimes.timestamp()   #<float>1542858901.0