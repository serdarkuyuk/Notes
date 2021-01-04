
## SQL
in schema.sql file, create a file for readable
```sql
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    city TEXT NOT NULL,
    clientIP TEXT NOT NULL,
    country TEXT NOT NULL,
    lat TEXT NOT NULL,
    lon TEXT NOT NULL,
    region TEXT NOT NULL,
    sentiment INTEGER NOT NULL,
    inputtext TEXT,
    timezone TEXT NOT NULL,
    weather TEXT NOT NULL,
    yelp TEXT
);
```

## reading sql and inserting first row
```python
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts(id, created, city, clientIP, country, lat, lon, region, sentiment, inputtext, timezone, weather, yelp) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (1, "04:09:2010", "Wilmington", "73.81.208.8", "US", "39.7460", "-75.5466",
             "Delaware", 1, "I feel lucky levent", "America/New_York", 'entry', 'entry')
            )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
# )

connection.commit()
connection.close()
```

## Special functions

```python
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def insertDatabase(output):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (city, clientIP, country, lat, lon, region, sentiment, inputtext, timezone, weather, yelp) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (output['city'], output['clientIP'], output['country'],
                  output['lat'], output['lon'], output['region'], output['sentiment'], output['inputtext'], output['timezone'], str(output['weather']), str(output['yelp'])))

    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.commit()
    conn.close()
    return posts


posts = insertDatabase(output)

@app.route('/database', methods=['GET', 'POST'])  # , methods=['POST'])
def database():
    databaseDict = {}
    if request.method == 'POST':
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        for i in posts:
            databaseDict[i['id']] = [i['id'], i['created'], i['city'], i['clientIP'], i['country'],
                                     i['lat'], i['lon'], i['region'], i['sentiment'],
                                     i['inputtext'], i['timezone'], str(i['weather']), str(i['yelp'])]
    return jsonify(databaseDict)


```
