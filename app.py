import ast

from flask import Flask, render_template
import requests
import json

endpoint = "http://127.0.0.1:8000"

app = Flask(__name__)

headers = {
    "Content-Type": "application/json"
}


@app.route('/play')
def hello_world():  # put application's code here
    query = requests.get(f"{endpoint}/getquery/", headers=headers).content.decode("utf-8").replace('"','')
    answers = ast.literal_eval(requests.get(f"{endpoint}/query/{query}", headers=headers).content.decode("utf-8"))["answers"]
    return render_template('play.html', query=query, answers=answers)


if __name__ == '__main__':
    app.run(Debug=True)
