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
    oldAnswers = ast.literal_eval(requests.get(f"{endpoint}/query/{query}", headers=headers).content.decode("utf-8"))["answers"]

    answers = []
    y = 0

    for i in oldAnswers:
        if y < 10:
            modified_i = i.replace(query.lower(), '')
            answers.append(modified_i)
            y += 1
            print(query.lower())
            print(answers)
            print(oldAnswers)

    return render_template('play.html', query=query, answers=answers)


if __name__ == '__main__':
    app.run(Debug=True)
