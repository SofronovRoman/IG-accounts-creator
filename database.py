
import sqlite3


# the class for work with database of accounts
class Database:
    @staticmethod
    def create_db():
        con = sqlite3.connect('accounts.db')
        with con:
            con.execute("""CREATE TABLE IF NOT EXISTS accounts(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               username TEXT,
               email TEXT,
               password TEXT,
               all_cookies TEXT,
               UA TEXT);""")

    @staticmethod
    def save_data_to_db(date, username, email, password, all_cookies, UA):
        con = sqlite3.connect('accounts.db')
        sql = """INSERT INTO accounts(date, username, email, password, all_cookies, UA) VALUES(?, ?, ?, ?, ?, ?);"""
        res = (date, username, email, password, all_cookies, UA)
        with con:
            con.execute(sql, res)
        print('Данные записаны в БД')








