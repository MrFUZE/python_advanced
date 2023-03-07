from flask import Flask

app = Flask(__name__)

@app.route('/counter')
def page_counter():
    page_counter.count += 1
    return f"Эта страница была открыта {page_counter.count} раз."

page_counter.count = 0

if __name__ == '__main__':
    app.run(debug=True)
