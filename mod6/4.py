import json
import itertools
import re
from collections import Counter

# Define the log levels we are interested in
LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

# Open the log file and read all lines
with open('skillbox_json_messages.log') as f:
    lines = f.readlines()

# Parse each line as JSON and filter for relevant logs
logs = []
for line in lines:
    try:
        log = json.loads(line)
        if log['level'] in LEVELS:
            logs.append(log)
    except json.JSONDecodeError:
        pass

# Task 1: Count the number of messages of each level
level_counts = Counter(log['level'] for log in logs)
print("Количество сообщений по уровням:", level_counts)

# Task 2: Find the hour with the most logs
hour_counts = Counter(log['time'][:2] for log in logs)
most_common_hour, num_logs = hour_counts.most_common(1)[0]
print("Час с наибольшим количеством логов:", most_common_hour)

# Task 3: Count the number of CRITICAL logs between 05:00:00 and 05:20:00
critical_logs = [log for log in logs if log['level'] == 'CRITICAL']
critical_logs_in_timeframe = [log for log in critical_logs if '05:00:00' <= log['time'] <= '05:20:00']
num_critical_logs = len(critical_logs_in_timeframe)
print("Количество CRITICAL логов между 05:00:00 и 05:20:00:", num_critical_logs)

# Task 4: Count the number of messages containing the word "dog"
num_messages_with_dog = sum(1 for log in logs if re.search(r'\bdog\b', log['message'], re.IGNORECASE))
print("Количество сообщений, содержащих слово 'dog':", num_messages_with_dog)

# Task 5: Find the word that appears most frequently in WARNING level messages
warning_messages = [log['message'] for log in logs if log['level'] == 'WARNING']
words = re.findall(r'\b\w+\b', ' '.join(warning_messages), re.IGNORECASE)
word_counts = Counter(words)
most_common_word, num_occurrences = word_counts.most_common(1)[0]
print("Наиболее часто встречающееся слово в сообщениях WARNING :", most_common_word)
