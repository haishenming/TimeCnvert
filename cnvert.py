'''
Created on 2017年11月06日 下午2:15

@author: xiangyufan@juwang.cn

'''

import time
from datetime import datetime

def strtime_to_inttime(t):
    """  字符串时间转换为时间戳
            “2017-01-02 00:00:00” 或 “2017-01-02”
    """
    # 将其转换为时间数组
    try:
        structtime = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        structtime = time.strptime(t, "%Y-%m-%d")

    # 转换为时间戳:
    inttime = int(time.mktime(structtime))

    return inttime



def strtime_to_datetime(t):
    """ 字符串时间转换为datatime实例
    """
    try:
        dtime = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        dtime = datetime.strptime(t, "%Y-%m-%d")

    return dtime

def inttime_to_strtime(t):
    """ 时间戳转换为字符串时间
    """
    struttime = time.localtime(t)
    strtime = time.strftime("%Y-%m-%d %H:%M:%S", struttime)

    return strtime

def inttime_to_datetime(t):
    """ 时间戳时间转化为datatime实例
    """
    dtime = datetime.fromtimestamp(t)

    return dtime

def datetime_to_inttime(t):
    """ datatime实例转换为时间戳
    """
    inttime = time.mktime(t.timetuple())

    return int(inttime)

def datetime_to_strtime(t):
    """ datatime实例转换为字符串时间
    """
    strtime = t.strftime("%Y-%m-%d %H:%M:%S")

    return strtime


if __name__ == '__main__':
    t1 = "2017-1-1"
    t2 = '2017-01-01'
    t3 = '2017-1-1 14:16:0'
    t4 = '2017-01-01 04:16:00'
    # inttime = strtime_to_inttime(t3)
    dtime = strtime_to_datetime(t3)
    # inttime_to_strtime(inttime)
    # inttime_to_datetime(inttime)
    # datetime_to_inttime(dtime)
    datetime_to_strtime(dtime)