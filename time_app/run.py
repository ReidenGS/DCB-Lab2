from flask import Flask,jsonify
from datetime import datetime,timezone

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'
@app.get("/time")
def time():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return jsonify(time=now), 200

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
