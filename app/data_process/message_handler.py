#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import jieba.posseg as pseg
import app
from app.functions import api_func, common_func, listen_func, clock_func


def handle_message(data, func):
    """

    :param data:
    :param func:
    :return:
    """
    message = data['message']
    sender_id = data['sender']['user_id']
    word_list, pop_list = [], []  # 分词以及词性列表
    for m in message:
        if m['type'] == 'text':
            temp = pseg.cut(m['data']['text'])
            for x in temp:
                x = tuple(x)
                word_list.append(x[0])
                pop_list.append(x[1])
            word_list.append(' ')
            pop_list.append('x')
        elif m['type'] == 'face':
            pass

    if not word_list:  # 如果没有文字（可能是文件或者语音）
        return
    if word_list[0] != '#' or sender_id not in app.authorized_users:
        return
    print(word_list)

    call_functions(word_list, pop_list, func, data)


def call_functions(word_list: list, pop_list: list, api_function, data):
    sender_id = data['sender']['user_id']  # 发送者
    target_id = data['sender']['user_id']  # 要发给谁
    if api_function.__name__ == api_func.send_group.__name__:
        target_id = data['group_id']
    elif api_function.__name__ == api_func.send_discuss.__name__:
        target_id = data['discuss_id']

    word_package = [word_list[:-1], pop_list[:-1]]
    # 首先监听功能取得消息并处理
    for func in app.work_fun_list:
        if func[0]:  # 如果是打开状态
            t = threading.Thread(
                target=func[1], name=str(func[1]), args=(word_package,))
            t.start()
            app.listen_thread_list.append(t)
    # 等待所有的监听型函数线程完成
    for t in app.listen_thread_list:
        t.join()
    app.listen_thread_list = []  # 清空列表

    if '菜单' == word_list[2]:  # 列出现有的功能
        reply = common_func.show_menu()
        api_function(sender_id, reply)
    elif "列出状态" == word_list[2]:  # 列出监听型函数的状态
        pass
    elif '天气' in word_list:
        reply = common_func.get_weather(word_list)
        api_function(target_id, reply)
    elif sender_id == app.robot_admin and '用户' in word_list:
        reply = common_func.manage_privilege(word_package)
        api_function(sender_id, reply)
    elif '配置' in word_list and '保存' in word_list:
        reply = common_func.save_current_config()
        api_function(sender_id, reply)
