#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import utils
import requests


async def chat_content(message):
    # 聊天的API地址    
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数  
    message = message.encode('utf-8')
    payload = utils.get_params(question=message, session='10000')
    # r = requests.get(url, params=payload)    
    r = requests.post(url, data=payload)
    if int(r.json()['ret']) != 0:
        return "不听不听"
    return r.json()["data"]["answer"]


async def translation_content(target_language, message):
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate"
    language_dict = {
        "日语": 'jp',
        "英语": 'en',
        "韩语": 'kr'
    }
    message = message.encode('utf-8')
    target_language = language_dict[target_language]
    payload = utils.get_params(target=target_language, source='zh', text=message)
    r = requests.post(url, data=payload)
    if int(r.json()['ret']) != 0:
        return "我不会吖(ㄒoㄒ)"
    return r.json()["data"]["target_text"]
