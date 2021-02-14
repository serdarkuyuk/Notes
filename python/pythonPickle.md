
if panda data frames
data_clean.to_pickle('data_clean.pkl')

with open('traininData.pickle', 'rb') as file:
    mytweet = pickle.load(file)

if it is other type
pickle.dump(cv, open("cv.pkl", "wb"))


## to dump a model
pickle.dump(clf, open("pipeline.pickle", "wb"))

## to load the model
file = open('pipeline.pickle', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

#pickle.dump(clf, open("pipeline.pickle", "wb"))

# streamlit or heroku procedure

```python
import pickle

#to create
pickle.dump(clf, open("pipeline.pickle", "wb"))

#to load
file = open('pipeline.pickle', 'rb')

# dump information to that file
mytest = pickle.load(file)

# close the file
file.close()
```

# using external functions or classes...
- create a folder, put your class in it
- import your class before running train...
- call this class in your web app...
