import os
import psycopg2 as p


class DbHelper:

    def get_db_connection(db_user, db_pass, url, port):
        with open('query.sql') as sql:
            query = sql.read()

        return p.connect(
            user=db_user,
            password=db_pass,
            host=url,
            port=port,
            database='SOMEDB',
            connect_timeout=10
        )

    def read_from_table(conn):
        try:
            with open('query.sql') as sql:
                query = sql.read()
            # Create cursor, execute the query, and fetch results
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
