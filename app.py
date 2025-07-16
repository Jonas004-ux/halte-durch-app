from flask import Flask, render_template, request, redirect, jsonify
import json
from datetime import datetime
import uuid

app = Flask(__name__)

DATA_FILE = 'messages.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hilfe')
def help_page():
    return render_template('help.html')

@app.route('/unterstuetzen')
def support_page():
    return render_template('support.html')

@app.route('/post_message', methods=['POST'])
def post_message():
    data = load_data()
    msg = {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'situation': request.form['situation'],
        'responses': []
    }
    data.insert(0, msg)
    save_data(data)
    return redirect('/hilfe')

@app.route('/post_response/<msg_id>', methods=['POST'])
def post_response(msg_id):
    data = load_data()
    for msg in data:
        if msg['id'] == msg_id:
            msg['responses'].append(request.form['response'])
            break
    save_data(data)
    return redirect('/unterstuetzen')

@app.route('/get_messages')
def get_messages():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(debug=True)
