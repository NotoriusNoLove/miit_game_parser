import sqlite3
import time

from dataparse.game_parser import game_parser
conn = sqlite3.connect('orders.db')
cur = conn.cursor()


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(
            f'[*] Время выполнения: {end-start} секунд.')
    return wrapper


def create_table():
    with conn:
        cur.execute("""CREATE TABLE IF NOT EXISTS info_game(
        userid INT,
        fname TEXT,
        lname TEXT,
        gender TEXT);
        """)
        conn.commit()


@benchmark
def insert(number):
    with conn:
        user = game_parser(number)

        cur.executemany("INSERT INTO info_game VALUES(?, ?, ?, ?);", user)

        conn.commit()


def get_all():
    cur.execute("SELECT * FROM info_game;")
    one_result = cur.fetchall()
    return one_result


if __name__ == "__main__":
    get_all()
