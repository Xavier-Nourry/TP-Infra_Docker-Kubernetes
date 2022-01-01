from flask import Flask
import requests
import mariadb
import sys



app = Flask(__name__)


def check_activity_in_db(activity):
    nb_lines = cur.execute(
    "SELECT * FROM activities WHERE description=(%s)", (activity,))
    print("nb_lines : " + str(nb_lines))
    if nb_lines != None:
        query_affected_lines = cur.execute("UPDATE activities SET nbOccurrences = nbOccurrences + 1 WHERE description=?", activity)
        conn.commit()
        print("Update query") 
    else:
        query_affected_lines = cur.execute("INSERT INTO activities (description, nbOccurrences) VALUES (%s, %d)", (activity, 1))
        conn.commit()
        print("Insert query")


@app.route("/")
def hello_world():
    url = 'http://www.boredapi.com/api/activity/'
    response = requests.get(url)
    data = response.json()
    activity = data["activity"]
    html = "<h1>Activité du jour</h1><br><h3>" + activity + "</h3>"
    check_activity_in_db(activity)
    generate_html()
    return html

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