#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


def fun1(d, t: str):
    """
    获取时间
    :param d:几天后
    :param t: 几时几分 xx:xx
    :return: datetime
    """
    now_time = datetime.now()
    temp_time = now_time + timedelta(days=d)
    index_num = t.index(':')
    target_time = datetime(temp_time.year,temp_time.month,temp_time.day, int(t[:index_num]), int(t[index_num+1:]), 0)
    res = target_time.timestamp() - now_time.timestamp()
    return int(res)


if __name__ == '__main__':
    # str1 = '10:00'
    # str2 = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    # str2 = str2[:6] + str1[:2] + str1[-2:] + str2[-2:]
    # dt = datetime.strptime(str2, '%Y%m%d%H%M%S')
    # print(dt)
    pass
