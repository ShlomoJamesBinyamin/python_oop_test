from iquerry import IQuerry
import sqlite3
from log_files.logger import log

class CreateQuery(IQuerry):

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        log.info("connection established")

    def connect(self):
        self.cursor = self.conn.cursor()
        log.info("cursor established")

    def commit(self, query, params=None):
        self.cursor.execute(query , params)
        self.conn.commit()
        log.info(f"running create query...")

    def fetch_results(self):
        pass

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        log.info("connection closed")