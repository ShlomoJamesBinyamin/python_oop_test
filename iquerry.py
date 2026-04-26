from abc import ABC, abstractmethod
from logger import log

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
    def commit(self, query):
        pass
    @abstractmethod
    def fetch_results(self):
        pass
    @abstractmethod
    def close_connection(self):
        pass

    def run(self,query):
        self.create_connection()
        self.connect()
        self.commit(query)
        self.fetch_results()
        self.close_connection()
        log.info(f"query: \n{query}\n occurred successfully")
