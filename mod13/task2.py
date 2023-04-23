import csv
import sqlite3

def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    # Read the data from the CSV file
    with open(wrong_fees_file, 'r') as f:
        reader = csv.reader(f)
        wrong_fees = list(reader)

    # Delete the records from the table_fees table
    for date, license_number in wrong_fees:
        cursor.execute(
            'DELETE FROM table_fees WHERE timestamp = ? AND truck_number = ?',
            (date, license_number)
        )

if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
