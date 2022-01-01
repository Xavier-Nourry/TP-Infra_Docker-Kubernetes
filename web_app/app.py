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
    cur.execute("SELECT * FROM activities WHERE description=(%s)", (activity,))
    nb_lines = get_altered_lines_after_request()
    print("nb_lines : " + str(nb_lines))
    if nb_lines != 0:
        cur.execute("UPDATE activities SET nbOccurrences = nbOccurrences + 1 WHERE description=(%s)", (activity,))
        conn.commit()
        print("Update query") 
    else:
        cur.execute("INSERT INTO activities (description, nbOccurrences) VALUES (%s, %d)", (activity, 1))
        conn.commit()
        print("Insert query")

def generate_html(activity):
    res = "<h1>Tip of the day</h1><h3>" + activity + "</h3><br><h3>All tips in time</h3>"
    cur.execute("SELECT description, nbOccurrences FROM activities")
    for (desc, occurrences) in cur:
        res += "<p>{d} : {o}</p><br>".format(d=desc, o=occurrences)
    return res

@app.route("/")
def hello_world():
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
            password="mypass",
            host="127.0.0.1", #"172.17.0.2", # Ou 127.0.0.1, à voir
            port=3306,
            database="TP_INFRA"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    app.run()