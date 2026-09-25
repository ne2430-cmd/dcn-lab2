from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return "Sample Time App is running. Visit /time to see the current time."


@app.route('/time')
def get_time():
    now = datetime.now()
    return f"Current server time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
