#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jieba.posseg as pseg
import hashlib
import time
import random
import string
from urllib.parse import quote
import app


async def word_cut(text_message):
    word_list, pop_list = [], []  # 分词以及词性列表
    temp = pseg.cut(text_message)
    for x in temp:
        x = tuple(x)
        word_list.append(x[0])
        pop_list.append(x[1])
    word_list.append(' ')
    pop_list.append('x')
    return word_list, pop_list


class Constant:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key: str, value):
        if key in self.__dict__:
            raise self.ConstError("Can't change const %s" % key)
        if not key.isupper():
            raise self.ConstCaseError(
                "const name %s is not all uppercase" % key)
        self.__dict__[key] = value


# 将得到的MD5值所有字符转换成大写
def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()


def get_params(**kwargs):
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）  
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测  
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key  
    app_id = app.app_id
    app_key = app.app_key
    # 基本参数
    params = {'app_id': app_id,
              'session': '10000',
              'time_stamp': time_stamp,
              'nonce_str': nonce_str}
    # 填充参数
    for key, value in kwargs.items():
        params[key] = value
    # 要对key排序再拼接  
    sign_before = ''
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，quote默认大写。  
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾  
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名  
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params
