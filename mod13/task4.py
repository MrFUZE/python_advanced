import sqlite3


def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str):
    cursor.execute("SELECT salary FROM table_effective_manager WHERE name = 'Иван Совин'")
    ivan_salary = cursor.fetchone()[0]

    cursor.execute(f"SELECT name, salary FROM table_effective_manager WHERE name LIKE '{name}'")
    employee_data = cursor.fetchone()

    if employee_data is None:
        print(f"Не найден сотрудник с именем '{name}'.")
        return

    employee_name, employee_salary = employee_data

    if employee_salary > ivan_salary:
        cursor.execute(f"DELETE FROM table_effective_manager WHERE name LIKE '{employee_name}'")
        print(f"Уволен сотрудник '{имя_работника}' из-за того, что его зарплата была выше зарплаты Ивана Совина.")
    elif employee_salary * 1.1 <= ivan_salary:
        new_salary = int(employee_salary * 1.1)
        cursor.execute(f"UPDATE table_effective_manager SET salary = {new_salary} WHERE name LIKE '{employee_name}'")
        print(f"Увеличение зарплаты сотрудника '{employee_name}' с {employee_salary} до {new_salary}.")
    else:
        print(f"Невозможно увеличить зарплату сотрудника '{employee_name}' так как она превысит зарплату Ивана Совина.")



if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        employee_name = input("Введите ФИО сотрудника в формате (Иванов И.И.): ")
        ivan_sovin_the_most_effective(cursor, employee_name)
