import sqlite3
import datetime


create_table_if_not_exist = """
CREATE TABLE IF NOT EXISTS table_with_birds(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       bird_name TEXT NOT NULL,
       date_when_added TEXT NOT NULL);
"""

def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
    cursor.execute("INSERT INTO table_with_birds (bird_name, date_when_added) VALUES (?, ?)", (bird_name, date_time))

def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute("SELECT EXISTS(SELECT 1 FROM table_with_birds WHERE bird_name = ?)", (bird_name,))
    return cursor.fetchone()[0]


if __name__ == "__main__":
    print(''' __     __          _            ___  __
 \ \   / /         | |          / _ \/_ |
  \ \_/ / __   __ _| |_  __   _| | | || |
   \   / '_ \ / _` | __| \ \ / / | | || |
    | || | | | (_| | |_   \ V /| |_| || |
    |_||_| |_|\__,_|\__|   \_/  \___(_)_|''')
    name = input("Пожалуйста введите имя птицы\n> ")
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_if_not_exist)
        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу вы уже наблюдали!")
        else:
            log_bird(cursor, name, right_now)
            print("Птица добавленна в базу")
