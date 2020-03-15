#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import jieba
import json
from app.utils import Constant

# 定义存储常量
constant = Constant()
constant.APP_PATH = os.path.dirname(os.path.dirname(__file__))  # .../qq_robot
# 加载插件路径
constant.PLUGINS_PATH = "app.plugins"
# 加载字典路径
constant.DICT_FILE = constant.APP_PATH + "/app/res/user_dict.txt"
# 这里换成你的设置
constant.CONFIG_PATH = constant.APP_PATH + "/app/res/my_config.json"
# 用户音乐列表（暂时还没用上）
constant.USER_MUSIC_LIST_PATH = constant.APP_PATH + "/app/res/user_music_list/"
# 加载配置
with open(constant.CONFIG_PATH, 'r') as f:
    configs = json.load(f)

jieba.load_userdict(constant.DICT_FILE)
# 用于qq api应用
app_id = configs["app_id"]
app_key = configs["app_key"]

if __name__ == '__main__':
    print(constant.CONFIG_PATH)
    pass
