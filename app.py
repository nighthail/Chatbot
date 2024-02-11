from flask import Flask, render_template, request as flask_request, jsonify
import chatapp
import sys

if sys.stdout.encoding is None or sys.stdout.encoding == 'ANSI_X3.4-1968':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')
if sys.stderr.encoding is None or sys.stderr.encoding == 'ANSI_X3.4-1968':
    sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf-8')

res = "Hello there brother!"
msg = ''

# bot_messages.clear()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get', methods=['POST'])
def get_response():
    global res, msg
    if flask_request.method == 'POST':
        try:
            msg = flask_request.form["msg"]
            res = chatapp.chatbot_response(msg)
        except Exception as e:
            return f"Error: {e}"

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
