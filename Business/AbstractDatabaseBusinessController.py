from abc import abstractmethod

from sqlalchemy.dialects.postgresql import psycopg2


class AbstractDatabaseBusinessController:
    def __init__(self):
        conn = psycopg2.connect(host="localhost", user="postgres", password="root")
        conn.autocommit = True

    @abstractmethod
    def Select(self):
        pass

    @abstractmethod
    def Insert(self):
        pass

    @abstractmethod
    def Update(self):
        pass