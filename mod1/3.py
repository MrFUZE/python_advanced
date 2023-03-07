import random
from flask import Flask

app = Flask(__name__)

cat_breeds = ['Cornish Rex', 'Russian Blue', 'Scottish Lop', 'Maine Coon', 'Munchkin']

@app.route('/cats')
def get_cat_breed():
    breed = random.choice(cat_breeds)
    return f"Random cat breed: {breed}"

if __name__ == '__main__':
    app.run(debug=True)
