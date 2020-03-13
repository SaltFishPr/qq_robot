#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.database.db_base import DBBase, execute_sql


class MusicDB(DBBase):
    @classmethod
    def add_music(cls, music_id, style, t):
        sql = "INSERT INTO musics (music_id, style, type) VALUES ('%d','%s', %s)" % (music_id, style, t)
        execute_sql(sql, 'insert')

    @classmethod
    def get_music_id_by_random(cls, style, t):
        sql = "SELECT music_id FROM musics WHERE style = '%s' AND type = '%s' ORDER BY RANDOM() limit 1" % (style, t)
        results = execute_sql(sql, 'select')
        return results

    @classmethod
    def get_all_styles(cls):
        sql = "SELECT style FROM musics GROUP BY style"
        results = execute_sql(sql, 'select')
        return results
