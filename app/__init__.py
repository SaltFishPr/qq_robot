#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import jieba
from app.utils import Constant

# 定义存储常量
constant = Constant()
constant.APP_PATH = os.path.dirname(os.path.dirname(__file__))  # .../qq_robot
constant.PLUGINS_PATH = "app.plugins"
constant.DICT_FILE = constant.APP_PATH + "/app/res/user_dict.txt"
constant.USER_MUSIC_LIST_PATH = constant.APP_PATH + "/app/res/user_music_list/"

jieba.load_userdict(constant.DICT_FILE)

if __name__ == '__main__':
    print(constant.APP_PATH)
    pass
