#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests


def a(**kwargs):
    print(type(kwargs), kwargs)


if __name__ == '__main__':
    d = {'app_key': "13145646", 'asad': "sald"}
    t = {}
    for key,value in d.items():
        t[key]=value
    print(t)
    pass
