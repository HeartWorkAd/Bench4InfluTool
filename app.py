from flask import Flask, render_template_string, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    chat_html_path = os.path.join(BASE_DIR, 'chat.html')
    with open(chat_html_path, 'r', encoding='utf-8') as f:
        chat_html = f.read()
    return render_template_string(chat_html)

@app.route('/conversations')
def conversations():
    conversations_path = os.path.join(BASE_DIR, 'conversations.json')
    with open(conversations_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)