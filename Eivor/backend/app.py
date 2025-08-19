from flask import Flask, render_template , jsonify
import os
from connections import db, collection

PORT = os.environ.get('PORT', 8000)

app = Flask(__name__)
    

@app.route('/')
def home():

    return jsonify({
        'message': 'Welcome to Eivor App'
    })

@app.route('/api/get')
def api():
    names = collection.find()
    result = []
    for name in names:
        result.append(name['value'])
    result = {
        'data': result
    }
    return jsonify(result)

@app.route('/api/add/<name>')
def add_name(name):
    collection.insert_one({"value": name})
    return jsonify({"message": f"{name} added successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
