import pandas
from dataclasses import dataclass

from .database.Database import Database


@dataclass
class Load:
    database: Database

    def start(self):
        self.database.start_connection()

    def end(self):
        self.database.close_connection()
