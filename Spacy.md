pip install -U spacy
pip install -U spacy lookups-data
python -m spacy download en_core_wev_sm

reference
https://kgptalkie.com/phone-number-email-emoji-extraction-in-spacy-for-nlp/

text --> tokenizer --> tagger --> parser --> ner --> custom --> spacyDoc
name        Tokinizer           ->  creates
tokenizer   Tagger              ->  doc
tagger      DependancyParser    ->  doc[i].head, doc[i].dep, doc[i].sents, doc[i].noun_chucks
ner         EntityRecognizer    ->  doc.ents, doc[i].ent_iob, doc[i].ent_type
textcat     TextCategorizer     ->  doc.cats


```python
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('my sentence here')
for token in doc:
    print(token.text)
token.text
token.lemma_

# part of speech
token.pos_
token.is_stop

# dependency parsing
for chunk in doc.noun_chunks:
    chunk.text, chunk.root.text, chunk.root.dep_

# NER
for ent in doc.ents:
    ent.text, ent.label_

# Sentence Segmentation
for sent in doc.sents:
    print(sent)

# set custom rule
def setRule(doc):
    for token in doc[:-1]:
        if token.text == '...'
            doc[token.i + 1].is_sent_start = True
    return doc

# remove pipe
nlp.remove_pipe('setRule')

# add pip
nlp.add_pipe(setRule, before='parser')

# visiualization
from spacy import displacy

displacy.render(doc, style='dep')

displacy.render(doc, style='dep', options={'compact':True, 'distance':100})

#for ner
displacy.render(doc, style='ner')

# probability vs

# rule-based matching
like regex

#  Token-based matching
PhraseMatcher object

# adding patterns
[{"LOWER":"hello"},{"IS_PUNCT": True}, {"LOWER":"world"}]

import spacy
from spacy.matcher import Matcher
from spacy.token import Span
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

doc = nlp("My sentence here, Hello World")

for token in doc:
    print(token)

#any combination of below
# 'OP':'?' means include or not
pattern = [{"LOWER":"hello" 'OP':'?'}, {"IS_PUNCT": True, 'OP':'?'}, {"LOWER":"world"}]

matcher = Matcher(nlp.vocab)
matcher.add('HelloWorld', None, pattern)

doc = nlp("Hello World!")
matches = matcher(doc)
print(matches)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings(match_id)
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)

# Regular Expression in Spacy    
text = 'Google announced a new Pixel at Google I/O. Google I/O is a great place to get all updates from Google'

pattern = [{'TEXT':'Google'}, {'TEXT':'I'},{'TEXT':'/'},{'TEXT':'O'}]

def callback_method(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    entity = doc[start:end]
    print(entity.txt)

matcher = Matcher(nlp.vocab)
matcher.add('Google', callbak_method, pattern)
doc = nlp(text)

matcher(doc)

pattern = [{'TEXT':'Google'}, {'TEXT':'I', 'OP':'?'},{'TEXT':'/', 'OP':'?'},{'TEXT':'O', 'OP':'?'}]
```


# Using Linguistic Annotation
```python
matcher = Matcher(nlp.vocab)

pattern = [{"LOWER", "facebook"},{"LEMMA": "be"},{"POS": "ADV", "OP":"*"},{"POS":"ADJ"}]

matched_sents = []
def callback_method_fb(matcher, doc, i, matches):
    matched_id, start, end = matches[i]
    span = doc[start:end]
    sent = span.sent

    match_ents = [{
        'start':span.start_char - sent.start_char,
        'end': span.end_char - sent.start_char,
        'label': 'MATCH'
        }]

    matched_sents.append({'text':sent.text, 'ents':match_ents})

matcher.add("fb", callback_method_fb, pattern)

doc = nlp("I'd say that Facebook is evil. - Facebook is pretty cool")

matches = matcher(doc)
print(matches)
print(matched_sents)

displacy.renter(matched_sents, style='ent', manual=True)
```
# phone numbers

```python
pattern = [{'ORTH':"("},{'SHAPE':"ddd"},{'ORTH':")"},{'SHAPE':"dddd"},{'ORTH':"-", "OP":"?"},{'SHAPE':"dddd"}]

matcher = Matcher(nlp.vocab)
matcher.add("Phonenumber", None, pattern)
doc = nlp('Call me at (123) 456 5342')
print([t.text for t in doc])
matches = matcher(doc)
print(matches)

for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

```

# Email address matching

```python
pattern = [{"TEXT":{'REGEX':"[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+"}}]

matcher = Matcher(nlp.vocab)
matcher.add("Email", None, pattern)

text = "Email me at email2me@interesting.com and talk2me@google.com"
doc = nlp(text)

mathces = matcher(doc)

for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

```

# Emoji matcing

```python
pos_emoji = ["😀", "😃", "😂", "🤣", "😊", "😍"]  # Positive emoji
neg_emoji = ["😞", "😠", "😩", "😢", "😭", "😒"]  # Negative emoji

# Add patterns to match one or more emoji tokens
pos_patterns = [[{"ORTH": emoji}] for emoji in pos_emoji]
neg_patterns = [[{"ORTH": emoji}] for emoji in neg_emoji]

def label_sentiment(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    if doc.vocab.strings[match_id] == 'HAPPY':
        doc.sentiment += 0.1
    elif doc.vocab.strings[match_id] == 'SAD':
        doc.sentiment -= 0.1

matcher = Matcher(nlp.vocab)
matcher.add("HAPPY", label_sentiment, *pos_patterns)
matcher.add('SAD', label_sentiment, *neg_patterns)
matcher.add('HASHTAG', None, [{'TEXT': '#'}, {'IS_ASCII': True}])

doc = nlp("Hello world 😀 #KGPTalkie")
matches = matcher(doc)

for match_id, start, end in matches:
    string_id = doc.vocab.strings[match_id]  # Look up string ID
    span = doc[start:end]
    print(string_id, span.text)

```

# Efficient phrase matching

```python
rom spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)
terms = ['BARAC OBAMA', 'ANGELA MERKEL', 'WASHINGTON D.C.']
pattern = [nlp.make_doc(text) for text in terms]
print(pattern)
matcher.add('term', None, *pattern)
doc = nlp("German Chancellor ANGELA MERKEL and US President BARAC OBAMA ",
          "converse in the Oval Office inside the White House in WASHINGTON D.C.")

print(doc)

matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

```

# Custom Rule based Entity Recognition

```python
from spacy.pipeline import EntityRuler
nlp = spacy.load('en_core_web_sm')
ruler = EntityRuler(nlp)
patterns = [{"label": "ORG", "pattern": "KGP Talkie"},
            {"label": "GPE", "pattern": [{"LOWER": "san"}, {"LOWER": "francisco"}]}]
patterns

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)
doc = nlp("KGP Talkie is opening its first big office in San Francisco.")
print(doc)

for ent in doc.ents:
    print(ent.text, ent.label_)

```

# Combining NLP Model and Custom Rules

```python
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

#loading english language model
nlp = spacy.load('en_core_web_sm')

doc = nlp('Dr. Alex Smith chaired first board meeting at Google')

print([(ent.text, ent.label_) for ent in doc.ents])

def add_title(doc):
   new_ents = []
   for ent in doc.ents:
       if ent.label_ == 'PERSON' and ent.start!=0:
           prev_token = doc[ent.start-1]
           if prev_token.text in ('Dr', 'Dr.', 'Mr', 'Mr.'):
               new_ent = Span(doc, ent.start-1, ent.end, label=ent.label)
               new_ents.append(new_ent)
           else:
               new_ents.append(ent)
   doc.ents = new_ents
   return doc

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(add_title, after='ner')

doc = nlp('Dr. Alex Smith chaired first board meeting at Google')   
print([(ent.text, ent.label_) for ent in doc.ents])
```

# Use of POS and Dependency Parsing


```python
nlp = spacy.load('en_core_web_sm')
doc = nlp('Alex Smith was working at Google')

displacy.render(doc, style='dep', options = {'compact':True, 'distance':100})

def get_person_orgs(doc):
    person_entities = [ent for ent in doc.ents if ent.label_=="PERSON"]
    for ent in person_entities:
        head = ent.root.head
        if head.lemma_ == 'work':
            preps = [token for token in head.children if token.dep_ == 'prep']
            for prep in preps:
                orgs = [token for token in prep.children if token.ent_type_ == 'ORG']
                print({'person': ent, 'orgs': orgs, 'past': head.tag_ == "VBD"})
    return doc

from spacy.pipeline import merge_entities
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(merge_entities)
nlp.add_pipe(get_person_orgs)
doc = nlp('Alex Smith worked at Google')

## Modify model
def get_person_orgs(doc):
    person_entities = [ent for ent in doc.ents if ent.label_=="PERSON"]
    for ent in person_entities:
        head = ent.root.head
        if head.lemma_ == 'work':
            preps = [token for token in head.children if token.dep_ == 'prep']
            for prep in preps:
                orgs = [token for token in prep.children if token.ent_type_ == 'ORG']

                aux = [token for token in head.children if token.dep_ == 'aux']
                past_aux = any(t.tag_ == 'VBD' for t in aux)
                past = head.tag_ == 'VBD' or head.tag_ == 'VBG' and past_aux

            print({'person': ent, 'orgs': orgs, 'past': past})   
    return doc

```

# Processing Pipeline


```python
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp('This is raw text')

texts = ["This is raw text", "There is lots of text"]
docs = list(nlp.pipe(texts))

import spacy

texts = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]

nlp = spacy.load("en_core_web_sm")
docs = nlp.pipe(texts, disable=["tagger", "parser"])
for doc in docs:
    # Do something with the doc here
    print([(ent.text, ent.label_) for ent in doc.ents])
    print()


nlp = spacy.load("en_core_web_sm", disable=["tagger", "parser"])
doc = nlp("Apple is buying a startup")
for ent in doc.ents:
    print(ent.text, ent.label_)

nlp = spacy.load("en_core_web_sm", disable=["tagger", "parser", "ner"])
doc = nlp("Apple is buying a startup")
for ent in doc.ents:
    print(ent.text, ent.label_)

nlp = spacy.load('en_core_web_sm')

# 1. Use as a contextmanager
with nlp.disable_pipes("tagger", "parser"):
    doc = nlp("I won't be tagged and parsed")
doc = nlp("I will be tagged and parsed")

# 2. Restore manually
disabled = nlp.disable_pipes("ner")
doc = nlp("I won't have named entities")
disabled.restore()
```

#
