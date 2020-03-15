# -*- coding: utf-8 -*-
# Created by: Michael Lan

import sqlite3 as sqlite


#----------------------------------------------------------------------
def connect(db):
    conn = sqlite.connect(db)
    return conn


#----------------------------------------------------------------------
def insert_data(conn, table, **kwargs):
    cursor = conn.cursor()

    fields = tuple(kwargs.keys())
    values = tuple(kwargs.values())
    cursor.execute(f"INSERT INTO {table} {fields} VALUES {values}")

    conn.commit()


#----------------------------------------------------------------------
def validate_duplicate(conn, table, field, value):
    cursor = conn.cursor()
    validation = cursor.execute(f'SELECT * FROM {table} WHERE {field} = {value}')
    if validation.fetchall():
        return True
    else:
        return  False


#----------------------------------------------------------------------
def close(conn):
    conn.close()


if __name__ == "__main__":
    conn = connect('dbCrokiAlitas.db')
    print(validate_duplicate(conn, 'users', 'dni', 1053832389))