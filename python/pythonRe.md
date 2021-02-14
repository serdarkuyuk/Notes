# REGEX

## Substition
return re.sub("[aeiou]+","",S)

^ start
. matches any character
[^] negater
* zero or more
+ one or more
{n,m} at least n and max m character
(xyz) exact order
\ escape the signal
$ end of character
? once or none - optional

\d digit
\w alphanumver
\s whitespace
\D not digit
\W none alphanumeric
\S not space

{3} occur exactly 3 times
{2,4} occurs 2 to 4 times
{3,} occurs 3 or more
\* occurs zero or more times
?

```python
text = "my phone numver is 1256. Ohh its wrong! Correct one is 1256348790. call me!"

import re
re.search(r'\d{10}', text)
#match object span, match= '1256348790'
re.search(r'\d{4}', text)
#match object span, match= '1256'
re.findall(r'\d{3,10}', text)
#digits with larger than 3 smallar than 10
re.findall(r'\w{4,}',text)
all alpanumerical larger than 4

# wildcard
re.finall(r'p....', text)
#phone

text = "this is cat but not that. i want hat and cat both"
re.findall(r'.a.', text)
# cat, hat, wan .....

text = '5hi thanks for watching <3'
re.findall(r'\d$', text) #3
re.findall(r'^\d', text) #5

#exclusions
re.findall(r'[^\d]')
#'hi thanks for watching <'
re.findall(r'[^\w]')
#[' ', ' ', .... '<'] all not alphanumeric values

text = 'you can get free-videos on kgp-interesting'
re.findall(r'[\w]+-[\w]+', text)
