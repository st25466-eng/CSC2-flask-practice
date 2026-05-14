import json 
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# all the route functions.
@app.route('/')
def home():
    flowers = load_data()
    addons = load_addons()
    return render_template('index.html', flowers=flowers, addons=addons)
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    return render_template("indext1.html")


def load_data():
    with open('data/flowers.json') as file:
        flowers = json.load(file)
    return flowers

def load_addons():
    with open('data/addons.json') as file:
        addons = json.load(file)
    return addons


if __name__ == '__main__':
    app.run(debug=True)
