import os
import random
import re
from flask import Flask

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_word_list():
    with open(BOOK_FILE, 'r') as book:
        text = book.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return words

WORDS = get_word_list()

@app.route('/get_random_word')
def random_word():
    word = random.choice(WORDS)
    return f"Случайное слово: {word}"

if __name__ == '__main__':
    app.run(debug=True)
