#!/usr/bin/python
# This Python file uses the following encoding: utf-8

from typing import List
import sqlite3

POS_DB = "data/pos_tags.db"
POS_TABLE = "tags"
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

    def getTags(self, word) -> List[str]:
        query = f'select group_concat({POS_TABLE_TAG_COL}) from (select distinct "{POS_TABLE_TAG_COL}" from "{self.pos_table}" where {POS_TABLE_WORD_COL}="{word}")'
        self.cursor.execute(query);
        result = self.cursor.fetchone()
        return [] if result is None or len(result) < 1 or result[0] is None else result[0].split(',')
