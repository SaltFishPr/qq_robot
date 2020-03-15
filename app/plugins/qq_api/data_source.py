#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import utils
import requests


def chat_content(message):
    # 聊天的API地址    
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数  
    message = message.encode('utf-8')
    payload = utils.get_params(question=message)
    # r = requests.get(url, params=payload)    
    r = requests.post(url, data=payload)
    return r.json()["data"]["answer"]
