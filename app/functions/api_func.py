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
