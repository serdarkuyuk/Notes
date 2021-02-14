
resources
https://www.youtube.com/watch?v=vR5utJvN4JY

# run XAMPP
start database etc...

# create a new envorinment
## Creating a virtual environment
> python3 -m venv env

## Activating a virtual environment

> source env/bin/activate

pip3 install mysql-connector-python-rf      



```python
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",
                               password="Workbench!1Aa", database="ABC")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)
```
