import sqlite3


conn = sqlite3.connect('hw_4_database.db')
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000")
poverty_count = c.fetchone()[0]
print(f"Количество людей за чертой бедности: {poverty_count}")

c.execute("SELECT AVG(salary) FROM salaries")
average_wage = c.fetchone()[0]
print(f"Средняя заработная плата: {average_wage}")

c.execute("SELECT AVG(salary) FROM (SELECT salary FROM salaries ORDER BY salary LIMIT 2 - (SELECT COUNT(*) FROM salaries) % 2 OFFSET (SELECT (COUNT(*) - 1) / 2 FROM salaries))")
median_wage = c.fetchone()[0]
print(f"Медианная заработная плата: {median_wage}")

count = c.execute("SELECT COUNT(salary) FROM salaries").fetchone()[0]
total = c.execute("SELECT SUM(salary) FROM salaries").fetchone()[0]
top10 = c.execute(f"SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {count})").fetchone()[0]
top90 = total - top10
F = round(top10/top90 * 100, 2)
print(f"Социальное неравенство на острове: {F}%")

conn.close()
