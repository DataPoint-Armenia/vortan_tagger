#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import sqlite3

POS_DB = "data/pos_tags.db"
POS_TABLE = "fiction"
POS_TABLE_WORD_COL = "phrase"
POS_TABLE_TAG_COL = "tag"

class tagger:
    def __init__(
        self,
        tags_db = POS_DB,
        pos_table = POS_TABLE,
    ):
        self.tags_db = tags_db
        self.pos_table = pos_table
        conn = sqlite3.connect(tags_db)
        self.cursor = conn.cursor()

    def getPOS(self, word):
        query = f'select "{POS_TABLE_TAG_COL}" from "{self.pos_table}" where {POS_TABLE_WORD_COL}="{word}"'
        self.cursor.execute(query);
        result = self.cursor.fetchone()
        return None if result is None or len(result) < 1 else result[0]
