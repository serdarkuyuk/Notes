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
