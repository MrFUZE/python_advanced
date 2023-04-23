import random
import sqlite3



countries = ['Испания', 'Франция', 'Германия', 'Италия', 'Англия', 'Нидерланды', 'Португалия', 'Бельгия', 'Аргентина', 'Бразилия', 'Россия']


sql_request_insert_teams = "INSERT INTO uefa_commands (command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?)"
sql_request_insert_draw = "INSERT INTO uefa_draw (command_number, group_number) VALUES (?, ?)"


def generate_test_data(cursor: sqlite3.Cursor, number_of_groups: int) -> None:
    teams = [(i+1, f'Team {i+1}', random.choice(countries), 'Сильная' if i%4==0 else 'Средняя' if i%4==1 or i%4==2 else 'Слабая') for i in range(number_of_groups*4)]
    random.shuffle(teams)

    groups = [[] for _ in range(number_of_groups)]
    for i in range(number_of_groups):
        strong_teams = [team for team in teams if team[3] == 'Сильная']
        medium_teams = [team for team in teams if team[3] == 'Средняя']
        weak_teams = [team for team in teams if team[3] == 'Слабая']
        groups[i].append(strong_teams.pop())
        groups[i].extend(random.sample(medium_teams, 2))
        groups[i].append(weak_teams.pop())
        random.shuffle(groups[i])

    draw = []
    used_numbers = set()
    for i, group in enumerate(groups):
        for team in group:
            command_number = team[0]
            while command_number in used_numbers:
                command_number += 1
            used_numbers.add(command_number)
            draw.append((command_number, i+1))

    cursor.execute("DELETE FROM uefa_commands")
    cursor.executemany(sql_request_insert_teams, teams)
    cursor.execute("DELETE FROM uefa_draw")
    cursor.executemany(sql_request_insert_draw, draw)



if __name__ == '__main__':
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    groups_count = int(input('Введите количество групп (от 4 до 16): '))

    generate_test_data(cursor, groups_count)
    conn.commit()
    conn.close()
