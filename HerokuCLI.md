# Heroku CLI

> https://devcenter.heroku.com/articles/heroku-cli

run in terminal
> brew tap heroku/brew && brew install heroku

restart terminal

activate virtual environment
> source yelp/bin/activate

> pip instal gunicorn

create an procfile
> touch Procfile
web: gunicorn app:app

## note
name of the file will be app.py

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])  # , methods=['POST'])
def main():

if __name__ == '__main__':
    app.run()

> pip freeze > requirements.txt

> git init

> git add .
> git commit -m "initial app"

## push to heroku- first login
> heroku login
login heroku on webpage

terminate ctrl+c

> heroku create

copy and paste the name and check the web browser

## changing the name
> heroku rename eldername

## push to heroku
> git push heroku master
