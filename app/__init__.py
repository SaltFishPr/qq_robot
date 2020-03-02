#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
from jieba import load_userdict
from app.utils import constant
from app.functions import listen_func, clock_func

# 常量命名
constant.APP_PATH = os.path.dirname(__file__)
constant.HOST = '127.0.0.1'  # 服务器ip
constant.API_PORT = 5700  # 调用api端口
constant.LISTEN_PORT = 5701  # 监听端口
constant.CONFIG_PATH = constant.APP_PATH + "/my_config.json"  # 配置文件路径
constant.USER_DICT_PATH = os.path.dirname(
    __file__) + "/res/user_dict.txt"  # 用户字典路径

# 加载变量
load_userdict(constant.USER_DICT_PATH)  # 加载user_dict.txt里的内容

with open(constant.CONFIG_PATH, 'r') as f:  # 加载config里的内容
    config = json.load(f)

robot_admin: int = config['robot_admin']  # 机器人管理员
authorized_users: list = config['user_list']  # 能够使用机器人的用户列表

listen_thread_list = []  # 监听型函数线程列表
clock_thread_list = []  # 定时器型函数线程列表

work_fun_list = [  # 所有工作型函数名的列表
    [False, listen_func.repeater]
]
clock_fun_list = [  # 所有定时器型函数名的列表

]
