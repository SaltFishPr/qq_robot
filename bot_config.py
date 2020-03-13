#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nonebot.default_config import *

# 超级用户
SUPERUSERS = {123456789}
# 命令开头为中文或者英文感叹号
COMMAND_START = {'!', '！'}
# nonebot.run()的ip和端口
HOST = '127.0.0.1'
PORT = 8080
# 机器人称呼，相当于@
NICKNAME = {'小Q'}
# 会话挂起持续时长
SESSION_EXPIRE_TIMEOUT = timedelta(seconds=30)
# 调用http api的ip和端口
API_ROOT = 'http://127.0.0.1:5700'
# 命令参数验证失败（验证器抛出 ValidateError 异常）、且验证器没有指定错误信息时，默认向用户发送的错误提示。
DEFAULT_VALIDATION_FAILURE_EXPRESSION = "请查看帮助检查输入~"
# 参数验证失败超过三次
TOO_MANY_VALIDATION_FAILURES_EXPRESSION = ["输错太多次啦，有需要再叫我吖~"]
# 结束当前会话的提示
SESSION_CANCEL_EXPRESSION = ["那我先去玩啦~", "拜拜~"]
# 当前还有会话正在进行时给用户的回复
SESSION_RUNNING_EXPRESSION = '还没说完呢！'
