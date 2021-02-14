# Mango DB

Not Only SQL
NoSQL

Collections (table)
Documents is a row in table

Document not always structured in the same way.

Document has key and value pairs
{FirstName : "Serdar",
LastName: "Kuyuk"}

Install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

install mongodb
brew install mongodb/brew/mongodb-community-shell

mongo "mongodb+srv://proteincluster.swwn5.mongodb.net/NAMEOFTHEDATABASE" --username serdar

check if mongoimport tools available
 ls "$(which mongo | sed 's/mongo//')" | grep mongo

if not:
brew install mongodb/brew/mongodb-database-tools


> use databaseName

db.protein.insertOne({"test":"1"})

db.protein.find()
db.protein.find().pretty()

db.protein.find({name:"serdar"}).pretty()

db.protein.find({name:"serdar"}).sort().pretty()

db.protein.find({name:"serdar"}).sort({firstname:1}).pretty() asc -1 desc
