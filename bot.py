#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nonebot 机器人启动文件
"""
from os import path

import nonebot

import my_bot_config
from app import constant

if __name__ == '__main__':
    nonebot.init(my_bot_config)
    plugin_num = nonebot.load_plugins(path.join(path.dirname(__file__), 'app', 'plugins'),
                                      constant.PLUGINS_PATH)
    print("成功加载{}个插件".format(plugin_num))
    nonebot.run()
