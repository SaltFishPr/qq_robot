#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import app.data_process
from flask import Flask, request
from app import constant

bot_server: Flask = Flask(__name__)


@bot_server.route('/api/message', methods=['POST'])
# 路径是你在酷Q配置文件里自定义的
def server():
    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    print(json.dumps(data, sort_keys=True, indent=4))  # 格式化输出json/字典
    app.data_process.data_unpack(data)
    return ''


if __name__ == '__main__':
    bot_server.run(port=constant.LISTEN_PORT)
