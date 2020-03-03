#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定时型函数由threading.Timer()创建，创建后与名字一起打包加入定时函数列表
"""
import re
import threading
from functools import reduce
from datetime import datetime, timedelta
import app


def analysis_create_clock(word_list: list, work_func, target_id):
    """

    :param word_list:
    :param work_func:
    :param target_id:
    :return:
    """
    try:
        words = reduce(lambda x, y: x + y, word_list)  # 连接字符串
        clock_time = re.findall(r'\d{1,2}:\d{1,2}', words)[0]  # 匹配出时间，只有一个时间所以取[0]
        index_num = word_list.index('提醒我')
        clock_id = int(word_list[-1])
        clock_content = reduce(lambda x, y: x + y, word_list[index_num + 1:-len(str(clock_id))])
    except ValueError:
        return '请检查输入再重新创建闹钟'

    if clock_time == '' or clock_content == '':
        return '请检查输入再重新创建闹钟'

    if clock_id in list(map(lambda x: x[1], app.clock_thread_list)):
        return "这个闹钟id已经存在"

    def fun1(d: int, t: str):
        """
        获取距离几天后几点还有多少秒
        :param d:几天后
        :param t: 几时几分 xx:xx
        :return: datetime
        """
        now_time = datetime.now()
        temp_time = now_time + timedelta(days=d)
        index_n = t.index(':')
        target_time = datetime(temp_time.year,
                               temp_time.month,
                               temp_time.day,
                               int(t[:index_n]),
                               int(t[index_n + 1:]),
                               0)
        res = target_time.timestamp() - now_time.timestamp()
        return int(res)

    def fun2(t: str):
        """
        距离t后还有多少秒
        :param t: 几小时几分钟 xx:xx
        :return:
        """
        index_n = t.index(':')
        now_time = datetime.now()
        target_time = now_time + \
                      timedelta(hours=int(t[:index_n]), minutes=int(t[index_n + 1:]))
        return int(target_time.timestamp() - now_time.timestamp())

    if '今天' in word_list:
        clock_time = fun1(0, clock_time)
    elif '明天' in word_list:
        clock_time = fun1(1, clock_time)
    elif '后' in word_list:
        clock_time = fun2(clock_time)

    if clock_time <= 0:
        return "闹钟不是时光机喔"

    if clock_content == 'xxx':
        pass
    else:
        create_clock(clock_time, clock_id, clock_content,
                     work_func, [target_id, clock_content])

    return "创建{}闹钟成功".format(clock_content)


def create_clock(
        clock_time,
        clock_id,
        clock_content,
        work_func,
        work_func_args: list):
    t = threading.Timer(clock_time, function=work_func, args=work_func_args)
    t.start()
    app.clock_thread_list.append([t, clock_id, clock_content])  # 将该线程存储到线程列表中


def analysis_remove_clock(word_list):
    clock_id_list = list(map(lambda x: x[1], app.clock_thread_list))
    clock_id = int(word_list[-1])
    index_num = clock_id_list.index(clock_id)
    clock_info = app.clock_thread_list[index_num]
    if clock_info[0].is_alive():  # 未运行过
        clock_info[0].cancle()  # 取消闹钟
    app.clock_thread_list.pop(index_num)
    return 'id：{}，{}闹钟已被清除'.format(clock_info[1], clock_info[2])


if __name__ == '__main__':
    pass
