from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    data = response.json()
    activity = data["activity"]
    return "<p>" + activity + "</p>"

if __name__ == '__main__':
    app.run()