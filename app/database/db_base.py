#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import os

database_path: str = os.path.dirname(__file__) + '/DB.sqlite'


def execute_sql(sql, choice):
    """
    执行sql语句
    :param sql:
    :param choice: 'select'， 'update', 'insert', 'delete'
    :return:
    """
    my_db = sqlite3.connect(database_path)
    my_cursor = my_db.cursor()
    my_cursor.execute(sql)
    results = []
    if choice == 'select':
        results = my_cursor.fetchall()
    else:
        my_db.commit()
    my_cursor.close()
    my_db.close()
    return results


class DBBase(object):
    @classmethod
    def get_info_by_dict(cls, table_name, args: dict):
        """
        根据传入的参数自动生成sql语句来查询
        :param table_name: 表名
        :param args: 传入dict，是tables
        :return: 根据选项获得表的所有信息
        """
        if args == {}:
            sql = "SELECT * FROM " + table_name
        else:
            sql1 = "SELECT * FROM " + table_name + " WHERE "
            keys = list(args.keys())
            values = list(args.values())
            sql2 = ""
            # 前面的参数后面要加AND
            for i in range(len(args) - 1):
                if isinstance(values[i], str):
                    sql2 = sql2 + keys[i] + " = \'" + values[i] + "\' AND "
                elif isinstance(values[i], int):
                    sql2 += keys[i] + " = " + str(values[i]) + " AND "
            # 最后一个参数后面不加AND
            if isinstance(values[-1], str):
                sql2 += keys[-1] + " = \'" + values[-1] + '\''
            elif isinstance(values[-1], int):
                sql2 += keys[-1] + " = " + str(values[-1])
            sql = sql1 + sql2
        results = execute_sql(sql, 'select')
        res = []
        for temp in results:
            res.append(list(temp))
        return res


if __name__ == '__main__':
    # print(database_path)
    pass
