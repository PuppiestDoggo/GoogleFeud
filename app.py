from flask import Flask, render_template
import requests
endpoint="http://127.0.0.1:8000"

app = Flask(__name__)


headers = {
    "Content-Type": "application/json"
}
@app.route('/play')
def hello_world():  # put application's code here
    query = requests.get(f"{endpoint}/getquery/", headers=headers).json()
    return render_template('play.html',query=query)

if __name__ == '__main__':
    app.run()
