#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


if __name__ == '__main__':
    with open(data_folder, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            print(type(data), data)
