#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nonebot 机器人启动文件
"""
import jieba
import nonebot
import my_bot_config
from os import path

if __name__ == '__main__':
    jieba.load_userdict("app/res/user_dict.txt")

    nonebot.init(my_bot_config)
    plugin_num = nonebot.load_plugins(path.join(path.dirname(__file__), 'app', 'plugins'),
                                      'app.plugins')
    print("成功加载{}个插件".format(plugin_num))
    nonebot.run()
