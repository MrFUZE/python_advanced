import sqlite3

def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    query = """
        SELECT EXISTS (
            SELECT * FROM table_truck_with_vaccine
            WHERE truck_number = ?
            AND timestamp >= datetime('now', '-3 hours')
            AND (temperature_in_celsius < -20 OR temperature_in_celsius > -16)
        )
    """
    cursor.execute(query, (truck_number,))
    result = cursor.fetchone()[0]
    return bool(result)


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        truck_number = input("Введите номер грузовика: ")
        print(check_if_vaccine_has_spoiled(cursor, truck_number))
