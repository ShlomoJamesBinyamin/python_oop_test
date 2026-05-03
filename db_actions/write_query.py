from db_actions.iquery import IQuery
import sqlite3
from log_files.logger import log

class WriteQuery(IQuery):
    # def __init__(self, db_name):
    #     super().__init__(db_name)

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        log.info("CONNECTION ESTABLISHED")

    def connect(self):
        self.cursor = self.conn.cursor()
        log.info("CURSOR APPLIED")

    def commit(self, query, params=None):
        self.rows= self.cursor.execute(query, params or ())
        self.conn.commit()
        log.info(f"RAN QUERY")

    def fetch_results(self):
        pass

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        log.info("CONNECTION CLOSED")