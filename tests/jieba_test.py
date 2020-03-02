#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jieba import posseg

if __name__ == '__main__':
    t = '嘻嘻 今天晚上我吃饭了'
    word_list = []
    pop_list = []
    temp = posseg.cut(t)
    for x in temp:
        x = tuple(x)
        word_list.append(x[0])
        pop_list.append(x[1])
    print(word_list, '\n', pop_list)
    pass
