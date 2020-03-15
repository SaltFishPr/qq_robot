#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
接收到消息后，先会判断前缀是否符合命令前缀，没有前缀抛出It's not a command异常，则忽略这句话。
如果有前缀，判断前缀后面跟的是否有已知的命令
前缀有存在的命令就直接进入@args_parser参数分析，之后再进入@on_command获取参数并处理，做出相应操作
没有存在的命令就忽略这句话
"""
from nonebot import on_command, CommandSession
from nonebot.command.argfilter import extractors, validators, converters, controllers  # 提取器，（剪切器自己定义函数），验证器，转换器，控制器
from nonebot import on_natural_language, NLPSession, IntentCommand

from app.utils import word_cut
from .data_source import get_weather_of_city, verifying_city


@on_command('查天气', aliases=('天气预报',))
async def weather(session: CommandSession):
    # 获得参数，如果没有这个参数，回复prompt等待用户补全参数
    # 注意，一旦传入arg_filters参数（参数过滤器），则等用户再次输入时，command_func.args_parser
    # 所注册的参数解析函数将不会被运行，而会在对current_arg依次运行过滤器之后直接将其放入state属性中。
    location = session.get('location', prompt="你想查询哪个城市的天气呢？")
    target_time = session.get('target_time', prompt="今天，明天，还是接下来五天？")
    weather_report = await get_weather_of_city(location, target_time)
    await session.send(weather_report)


# 询问补全命令参数
@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    # 如果是第一次进入命令, 填充已给参数
    if session.is_first_run:
        my_args = stripped_arg.split()
        if my_args:
            try:
                if await verifying_city(my_args[0]):
                    session.state['location'] = my_args[0]
            except IndexError:
                pass
            finally:
                return

    # 判断用户回复是否为空
    if session.current_key is not None and stripped_arg == '':
        # 需要连续接收用户输入，并且过程中不需要改变 current_key 时，使用此函数暂停会话。
        session.pause('我看不见啦！')

    if stripped_arg in ['算了', '不查了']:
        # 结束当前的会话
        session.finish("拜拜~")

    # 如果是在补全地点参数
    if session.current_key == 'location':
        if await verifying_city(stripped_arg):
            session.state['location'] = stripped_arg
        else:
            # 发送消息并暂停当前会话（该行后面的代码不会被运行
            session.pause('要查询的城市不存在呢，请重新输入')
    # 如果是在补全时间参数
    elif session.current_key == 'target_time':
        target_time = []
        if "今天" in stripped_arg:
            target_time.append("今天")
        if "明天" in stripped_arg:
            target_time.append("明天")
        if "接下来五天" in stripped_arg:
            target_time = ["接下来五天"]
        if not target_time:
            session.pause('时间格式不对哦')
        session.state['target_time'] = target_time


@on_natural_language(keywords={'天气怎么样'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    word_list, _ = await word_cut(stripped_msg)

    location = ""
    for word in word_list:
        if await verifying_city(word):
            location = word
            break

    target_time = []
    if "今天" in word_list:
        target_time.append("今天")
    if "明天" in word_list:
        target_time.append("明天")
    if not target_time:
        target_time.append("接下来五天")

    if location == '':
        return IntentCommand(80.0, name='查天气', args={'target_time': target_time})
    else:
        return IntentCommand(80.0, name='查天气', args={'target_time': target_time}, current_arg=location)
