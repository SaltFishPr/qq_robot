#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.database.db_base import DBBase, execute_sql


class CityDB(DBBase):
    @classmethod
    def add_city(cls, city_id, name):
        sql = "INSERT INTO cities (city_id,name) VALUES ('%d','%s')" % (
            city_id, name)
        execute_sql(sql, 'insert')

    @classmethod
    def search_city(cls, name):
        sql = "SELECT * FROM cities WHERE name = '%s'" % name
        results = execute_sql(sql, 'select')
        return results


if __name__ == '__main__':
    print(CityDB.search_city('北京'))
