from abc import abstractmethod

import psycopg2


class AbstractDatabaseBusinessController:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", user="postgres", password="root")
        self.conn.autocommit = True

    @abstractmethod
    def Select(self):
        pass

    @abstractmethod
    def SelectById(self, id):
        pass

    @abstractmethod
    def Insert(self, info):
        pass

    @abstractmethod
    def Update(self, info):
        pass