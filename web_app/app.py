from flask import Flask
import requests
import mariadb
import sys



app = Flask(__name__)


def get_altered_lines_after_request():
    res = 0
    for line in cur:
        res += 1
    return res

def check_activity_in_db(activity):
    cur.execute("SELECT * FROM Activities WHERE description=(%s)", (activity,))
    nb_lines = get_altered_lines_after_request()
    print("nb_lines : " + str(nb_lines))
    if nb_lines != 0:
        cur.execute("UPDATE Activities SET nbOccurrences = nbOccurrences + 1 WHERE description=(%s)", (activity,))
        conn.commit()
        print("Update query") 
    else:
        cur.execute("INSERT INTO Activities (description, nbOccurrences) VALUES (%s, %d)", (activity, 1))
        conn.commit()
        print("Insert query")

def generate_html(activity):
    res = "<h1>Tip of the day</h1><h4>" + activity + "</h4><br><h1>All tips in time</h1>"
    cur.execute("SELECT description, nbOccurrences FROM Activities")
    for (desc, occurrences) in cur:
        res += "<h4>{d} : {o}</h4>".format(d=desc, o=occurrences)
    return res

@app.route("/")
def index():
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    data = response.json()
    activity = data["activity"]
    check_activity_in_db(activity)
    return generate_html(activity)

if __name__ == '__main__':
    global cur, conn
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="root_password",
            host="database", #"172.17.0.2",
            port=3306,
            database="TP1_INFRA"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    app.run(host='0.0.0.0')