#Writing and reading

EOF end of file  character

```python

input = open(file, "r")
close(input)

#input is object, file handler

```

```python
fasta_file = "/user/serdar/Documents/udel/courses/binf690/hw4/contigs.fasta"
fastq_file = "name.fastq"
output = "out.fasta"

with open(fileName, 'r') as input, open(output, 'w') as output:
  pass

#no need to close(name) statement

input.seek(0,0)
input.readline()
```
```python
name = "serdar"
print('The youtube channel is {}'.format(name))
print(f'The youtube channel is {name}')

dataScience = [('python', 19),
                ('feature selection', 11),
                ('machine learning', 11),
                ('deep learnijng', 19)]

for info in dataScience:
    print(f'{info[0]:(50)} {info[1]:(10)}')
    print(f'{info[0]:<(50)} {info[1]:.>(10)}')
    #> right
    #< left
    #^ middle
    #. points
```

to read tsv tab separated file
```python
import pandas as pd
data = pd.read_csv('moviereviews.tsv', sep = '\t')

pos = data[data['label']='pos']
pos.to_csv('pos.tsv', sep = '\t'l, index = False)


## magic command in python %%writefile
%%writefile text1.txt
Hello text1kjlkj
jkhlfufghfh

%%writefile -a text1.txt
appending text


input = open('text1.txt', "r")
file.read()
file.readline() one line
file.readlines() # all one by one in a list line
file.close()

with open('text1.txt') as file:
    text_data = file.readlines()

for temp in text_data:
    print(temp.strip())


file = open('text1.txt', "w")
file.write("This is just another line")
file.close()

with open('text3.txt', 'w') as file:
    file.write('this is first line\n')
#append
with open('text3.txt', 'a') as file:
    for temp in text_data:
        file.write(temp)
