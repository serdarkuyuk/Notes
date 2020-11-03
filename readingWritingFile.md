#Writing and reading


```python

input = open(file, "r")
close(input)

#input is object, file handler

```

```python
fasta_file = "name.fasta"
fastq_file = "name.fastq"
output = "out.fasta"

with open(fileName, 'r') as input, open(output, 'w') as output:
  pass

#no need to close(name) statment

```
