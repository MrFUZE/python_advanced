import sqlite3

with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM table_1;")
    result = cursor.fetchone()
    print("Количество записей в table_1:", result[0])

    cursor.execute("SELECT COUNT(*) FROM table_2;")
    result = cursor.fetchone()
    print("Количество записей в table_2:", result[0])

    cursor.execute("SELECT COUNT(*) FROM table_3;")
    result = cursor.fetchone()
    print("Количество записей в table_3:", result[0])

    cursor.execute("SELECT COUNT(DISTINCT value) FROM table_1;")
    result = cursor.fetchone()
    print("Количество уникальных записей в table_1:", result[0])

    cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2);")
    result = cursor.fetchone()
    print("Количество записей из table_1, найденных в table_2:", result[0])

    cursor.execute("SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2) AND value IN (SELECT value FROM table_3);")
    result = cursor.fetchone()
    print("Количество записей из table_1, найденных в table_2 и table_3:", result[0])
