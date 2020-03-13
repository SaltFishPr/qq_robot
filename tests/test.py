#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests

if __name__ == '__main__':
    s = "上海 [1,2,3]"
    l = s.split()[1]
    print(type(json.loads(l)), json.loads(l))
    pass
