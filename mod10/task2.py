import sqlite3

try:
    with sqlite3.connect("hw_2_database.db") as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()


        query = "SELECT phone_color FROM table_checkout ORDER BY sold_count DESC LIMIT 1"
        result = cursor.execute(query).fetchone()
        if result:
            print(f"Больше всего продается телефонов цвета {result['phone_color']}")


        query = "SELECT phone_color, sold_count FROM table_checkout WHERE phone_color IN (?, ?) ORDER BY sold_count DESC"
        result = cursor.execute(query, ('Red', 'Blue')).fetchall()
        if len(result) > 1 and result[0]['sold_count'] == result[1]['sold_count']:
            print("Телефоны красного и синего цвета продаются одинаково")
        elif result:
            print(f"Телефонов цвета {result[0]['phone_color']} продается больше")


        query = "SELECT phone_color FROM table_checkout ORDER BY sold_count LIMIT 1"
        result = cursor.execute(query).fetchone()
        if result:
            print(f"Телефоны цвета {result['phone_color']} продаются реже всего")

except sqlite3.Error as e:
    print(f"Произошла ошибка: {e}")
