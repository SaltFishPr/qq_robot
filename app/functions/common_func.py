#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import math
from functools import reduce

import requests
import json
import app
from app import constant
from app.functions import api_func
from app.database.city_db import CityDB


# 获取天气信息
def get_weather(word_list: list):
    location = ""
    for x in word_list:
        if CityDB.search_city(x):
            location = x
            break
    if location == "":
        return "没有这个城市喔"

    data = requests.get(
        "http://wthrcdn.etouch.cn/weather_mini?city=%s" %
        location).text
    data = (json.loads(data))

    def arrange_info(choice, d):
        city = d['data']['city']
        res = ""
        if choice == '今天':
            today_data = d['data']['forecast'][0]
            res = "{choice}是{date}，{city}的最{high}，最{low}，天气{type}。".format(
                choice=choice, city=city, **today_data)
        elif choice == '明天':
            tomorrow_data = d['data']['forecast'][1]
            res = "{choice}是{date}，{city}的最{high}，最{low}，天气{type}。".format(
                choice=choice, city=city, **tomorrow_data)
        elif choice == '接下来五天':
            forecast = d['data']['forecast']
            info1 = "{date}：{type}，{high}，{low}；".format(**forecast[0])
            info2 = "{date}：{type}，{high}，{low}；".format(**forecast[1])
            info3 = "{date}：{type}，{high}，{low}；".format(**forecast[2])
            info4 = "{date}：{type}，{high}，{low}；".format(**forecast[3])
            info5 = "{date}：{type}，{high}，{low}；".format(**forecast[4])
            info6 = d['data']['ganmao']
            res = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
                city, info1, info2, info3, info4, info5, info6)
        return res

    res = ""
    if "今天" in word_list:
        res += arrange_info('今天', data) + "\n"
    if "明天" in word_list:
        res += arrange_info('明天', data) + "\n"
    if "今天" not in word_list and "明天" not in word_list:
        res = arrange_info('接下来五天', data) + "\n"
    res = res[:len(res) - 1]
    return res


# 管理用户
def manage_privilege(message_package: list):
    """
    处理信息调用用户管理的函数
    :param message_package:消息包，[词列表，词性列表]
    :return:
    """

    # 赋予权限
    def grant(user_id: int):
        app.authorized_users.append(user_id)

    # 收回权限
    def revoke(user_id: int):
        app.authorized_users.remove(user_id)

    # 列出用户列表
    def list_users():
        users = app.authorized_users
        reply = ""
        for x in users:
            reply += api_func.get_strange_info(int(x))['data']['nickname'] + '，'
        return "用户有：" + reply[:-1]

    if "列出" in message_package[0]:
        return list_users()

    index_num = message_package[1].index('m')
    target_id = int(message_package[0][index_num])
    if "增加" in message_package[0]:
        grant(target_id)
        return "增加用户成功"
    elif "移除" in message_package[0]:
        revoke(target_id)
        return "移除用户成功"


# 保存当前配置信息
def save_current_config():
    with open(constant.CONFIG_PATH, 'w') as f:
        json.dump(app.config, f, sort_keys=True, indent=4)
    return "保存配置成功"


# 输出机器人菜单
def show_menu():
    res = ""
    with open(constant.APP_PATH + "/res/menu.txt", 'r', encoding='utf-8') as f:
        for l in f:
            if l[0] == '×':
                continue
            res = res + l
    return res


# 列出所有函数的开关情况
def show_func_status():
    pass


# 列出订过的闹钟
def list_current_clocks():
    res = ''
    for t in app.clock_thread_list:
        if t[0].is_alive():
            res += '{}: {},\n'.format(t[1], t[2])
        else:
            app.clock_thread_list.remove(t)
    if res == '':
        res = '当前无任何闹钟  '
    return res[:-2]


# 列出正在监听的函数
def list_current_listen_func():
    pass


# 发张涩图
# def get_a_setu():
#     index_num = random.randint(0, len(app.setu_list) - 1)
#     setu_path = constant.SETU_PATH + '/' + app.setu_list[index_num]
#     res = "[CQ:music,type=163,id=28406557]".format(setu_path)
#     res = "[CQ:record,file=file:///F:/Programming/Python/qq_robot/app/res/audio/1.mp3]"
#     print(res)
#     return res


# 搜索歌曲 前十排行
def search_music(word_list: list):
    index_num = word_list.index(':') if ':' in word_list else word_list.index('：')
    music_name = reduce(lambda x, y: x + y, word_list[index_num + 1:])
    temp = api_func.get_top_ten_music(music_name)
    if temp is None:
        return "没有这首歌的信息"
    res = ""
    for music in temp:
        res += "专辑：{}，作者：{}，热度：{}，id:{}\n\n".format(music[0], music[2], math.ceil(int(music[3])/20.0) * "🔥", music[1])
    return res


# 通过id获取歌曲分享
def play_music(word_list):
    music_id = word_list[-1]
    res = "[CQ:music,type=163,id={}]".format(music_id)
    return res


if __name__ == '__main__':
    print(math.ceil(int(100)/20.0) * 'huo')
    pass
