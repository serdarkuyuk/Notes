Corpus = all documents
BOW = bag of word, all unique words without order preserved
vectorization

lets three documents
have 10 unique words
            WORD1 WORD2 WORD3....    WORD10  Target  (classification)
document 1     4    0     3                    football         <- document vectors
document 2     1    2     1            4       chess
document 3                                     basketball
counting the frequency of words
1. lots of zeros.
2. somewords are so frequent, we should normalize it

                WORD1     WORD2 WORD3....    WORD10     Target  (classification)
document 1     4/n(doc1)    0     3                     football         <- document vectors
document 2     1            2     1            4        chess
document 3                                              basketball  

word game can be occur in each document frequently so we should eleminate it

TF-IDF Term frequency, inverse document frequency



                        game    football    chess   basketball
document football       50          50
document chess          60                     50
document basketball     45                              50      

i - word
j - document
w(i,j) = frequency(i,j) x log( N / frequency(i in all documents) )

for document football
game = 50 x log (3 total numbers of documents / 3 (word game occur n documents) )
football = 50 x log (3 / 1 )

```python
from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = ["Aman is a data scientist in India","This is unfold data science","Data Science is a promising career"]
# create the transform
vectorizer = TfidfVectorizer()

# tokenize and build vocab
vectorizer.fit(text)
#Focus on IDF VALUES
print(vectorizer.idf_)
# summarize
print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform([text_as_input])
# summarize encoded vector
print(vector.toarray())

```
