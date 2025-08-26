from flask import Flask, render_template
import os
import requests



app = Flask(__name__)
PORT = os.environ.get('PORT', 5000)

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8000/api/get')
    

@app.route('/')
def home():
    try:
        response = requests.get(f'{BACKEND_URL}')
        response.raise_for_status()  # Raises HTTPError for bad responses
        try:
            data = response.json()
        except ValueError:
            data = {"error": "Invalid JSON from backend", "content": response.text}
    except requests.RequestException as e:
        data = {"error": str(e)}

    print("Data from backend:", data, type(data))

    env = dict(os.environ)
    print("Environment Variables:", env)
    return render_template('index.html', env=env, data=data)


if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=PORT)
