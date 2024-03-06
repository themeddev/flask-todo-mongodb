from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client['test_flask']  # actual database name
collection = db['users']  # actual collection name

@app.route('/')
def index():
    users = collection.find()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = int(request.form['age'])
    city = request.form['city']
    
    collection.insert_one({'name': name, 'age': age, 'city': city})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
