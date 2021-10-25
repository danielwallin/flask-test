from dataclasses import dataclass

import psycopg2
from psycopg2.extras import RealDictCursor

import config


@dataclass
class Database():
    conn: str = None
    host: str = config.DB_HOST
    username: str = config.DB_USER
    password: str = config.DB_PASS
    port: str = config.DB_PORT
    dbname: str = config.DB_NAME
    cursor: classmethod = None

    # create or get connection
    def connect(self):        
        if self.conn is None or self.conn.closed:
            print("connecting")
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname,
                    cursor_factory=RealDictCursor
                )
                self.cursor = self.conn.cursor()
            except psycopg2.DatabaseError as e:
                print(e)
                raise e
            finally:
                return self.conn
        else: 
            return self.conn    

    def execute(self, query, fetchmethod = None):
        try:
            con = self.connect()
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            if fetchmethod:
                return getattr(cursor, fetchmethod)()
        except (Exception) as error:
            print("Error while connecting to PostgreSQL", error)
            return error
        finally:
            if (self.conn):
                print("Closing connection")
                cursor.close()

    def fetchrows(self, query):
        return self.execute(query, 'fetchall')

    def fetchrow(self, query):
        return self.execute(query, 'fetchone')

    def insertrow(self, query):
        return self.execute(query)
