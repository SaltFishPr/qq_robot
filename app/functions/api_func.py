#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests

from app import constant


# 发送群组消息
def send_group(sender_id, info):
    data = {
        "group_id": sender_id,
        'message': info,
        'auto_escape': False
    }
    api_url = 'http://{}:{}/send_group_msg'.format(constant.HOST, constant.API_PORT)
    return json.loads(requests.post(api_url, data=data).text)


# 发送讨论组消息
def send_discuss(sender_id, info):
    data = {
        "discuss_id": sender_id,
        'message': info,
        'auto_escape': False
    }
    api_url = 'http://{}:{}/send_discuss_msg'.format(constant.HOST, constant.API_PORT)
    return json.loads(requests.post(api_url, data=data).text)


# 发送私聊
def send_private(sender_id, info):
    data = {
        "user_id": sender_id,
        'message': info,
        'auto_escape': False
    }
    api_url = 'http://{}:{}/send_private_msg'.format(constant.HOST, constant.API_PORT)
    return json.loads(requests.post(api_url, data=data).text)


# 获取陌生人信息
def get_strange_info(user_id):
    data = {
        "user_id": user_id,
        'no_cache': False
    }
    api_url = 'http://{}:{}/get_stranger_info'.format(constant.HOST, constant.API_PORT)
    return json.loads(requests.post(api_url, data=data).text)


# 获取网易云音乐歌曲信息
def get_top_ten_music(s, search_type=1, offset=0, limit=10):
    """
    post http://music.163.com/api/search/pc/?s={}&offset={}&limit={}&type={}
    :param s:
    :param search_type: 搜索方式  1:music 10:专辑 100:歌手 1000:歌单 1002:用户 1004:mv 1006:歌词
    :param offset: 从第offset个开始
    :param limit: 获取数量
    :return:[专辑名, 歌曲id, 作者名, 热度(分数)]
    """
    api_url = "http://music.163.com/api/search/pc/?s={}&offset={}&limit={}&type={}".format(s, offset, limit, search_type)
    data = json.loads(requests.post(api_url).text)
    if data['result']['songCount'] == 0:
        return None
    res = []
    for temp in data['result']['songs']:
        res.append([temp['album']['name'], temp['id'], temp['artists'][0]['name'], temp['popularity']])
    return res
