import os
import psycopg2

from repository import Repository


class PostgresRepository(Repository):

    def __init__(self):
        self.connection = psycopg2.connect(
            os.getenv("DATABASE_URL")
        )

    def add(self, text):

        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO messages(text) VALUES(%s)",
            (text,)
        )

        self.connection.commit()

        cursor.close()

    def get_all(self):

        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT id,text FROM messages"
        )

        rows = cursor.fetchall()

        cursor.close()

        result = []

        for row in rows:
            result.append({
                "id": row[0],
                "text": row[1]
            })

        return result