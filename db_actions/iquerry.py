from abc import ABC, abstractmethod
from log_files.logger import log

class IQuerry(ABC):
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.rows = None
        self.result = None

    @abstractmethod
    def create_connection(self):
        pass
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def commit(self, query, params=None):
        pass
    @abstractmethod
    def fetch_results(self):
        pass
    @abstractmethod
    def close_connection(self):
        pass

    def run(self,query, params=None):
        """orchestrates the query running procedure"""
        self.create_connection()
        self.connect()
        self.commit(query, params)
        self.fetch_results()
        self.close_connection()
        log.info(f"QUERY: \n{query}\n RAN SUCCESSFULLY")
        return self.result
