import copy
import datetime
import random
import sqlite3


class Employer:
    def __init__(self, id, name, preferable_sport):
        self.id = id
        self.name = name
        self.preferable_sport = preferable_sport


SPORT_DAY_DICT = {
    0: "футбол",
    1: "хоккей",
    2: "шахматы",
    3: "SUP сёрфинг",
    4: "бокс",
    5: "Dota2",
    6: "шах-бокс"
}


def get_employees(cursor):
    employees_list = []
    query = """
        SELECT * FROM table_friendship_employees
    """
    cursor.execute(query)
    res = cursor.fetchall()
    for employer in res:
        employees_list.append(Employer(
            id=employer[0],
            name=employer[1],
            preferable_sport=employer[2]
        ))
    return employees_list


def to_dict(employees):
    sport_dict = {}
    for employer in employees:
        sport_dict.setdefault(employer.preferable_sport, []).append(employer)
    return sport_dict


def get_sport_without_weekday(weekday_sport):
    num = random.randint(0, 6)
    sport = SPORT_DAY_DICT[num]
    while weekday_sport == sport:
        num = random.randint(0, 6)
        sport = SPORT_DAY_DICT[num]
    return sport


def update_work_schedule(cursor):
    employees = get_employees(cursor)
    rm = to_dict(employees)
    employees_dict_for_sport = copy.deepcopy(rm)
    schedule_parameters = []
    for day in range(1, 366):
        date = datetime.datetime(year=2020, day=1, month=1) + datetime.timedelta(days=day)
        weekday = date.weekday()
        weekday_sport = SPORT_DAY_DICT[weekday]
        for employer_num in range(10):
            sport = get_sport_without_weekday(weekday_sport)
            while not employees_dict_for_sport.get(sport):
                sport = get_sport_without_weekday(weekday_sport)
                if not employees_dict_for_sport.get(sport):
                    employees_dict_for_sport = copy.deepcopy(rm)
            employer = employees_dict_for_sport[sport].pop(0)
            schedule_parameters.append({
                "employee_id": employer.id,
                "date": date
            })
    query = f"""
        INSERT INTO table_friendship_schedule (employee_id, date) VALUES (
            :employee_id,
            :date
        )
    """
    cursor.executemany(query, schedule_parameters)
    cursor.connection.commit()


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        delete_query = "DELETE FROM table_friendship_schedule"
        cursor.execute(delete_query)
        update_work_schedule(cursor)
