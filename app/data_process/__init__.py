#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import app
from app.data_process.message_handler import handle_message
from app.functions import api_func


def data_unpack(data):
    """
    处理上报的数据，判断数据类型以及用户权限，调用base中的操作
    :param data:
    :return:
    """
    # 判断数据类型
    if data['post_type'] == 'message':
        # 判断权限
        if data['sender']['user_id'] not in app.authorized_users:  # 不在用户列表中无法使用机器人
            return

        if data['message_type'] == "group":  # 群消息
            handle_message(data, api_func.send_group)
        elif data['message_type'] == "private":  # 私聊
            handle_message(data, api_func.send_private)
        elif data['message_type'] == "discuss":  # 讨论组消息
            handle_message(data, api_func.send_discuss)

    elif data['post_type'] == 'notice':
        if data['notice_type'] == "group_upload":  # 群文件上传
            pass
        elif data['notice_type'] == "group_admin":  # 群管理员变动
            pass
        elif data['notice_type'] == "group_decrease":  # 群成员减少
            pass
        elif data['notice_type'] == "group_increase":  # 群成员增加
            pass
        elif data['notice_type'] == "group_ban":  # 群禁言
            pass
        elif data['notice_type'] == "friend_add":  # 好友添加
            pass

    elif data['post_type'] == 'request':
        if data['request_type'] == "friend":  # 加好友请求
            pass
        elif data['request_type'] == "group":  # 加群请求
            pass


if __name__ == '__main__':
    pass
