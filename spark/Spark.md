# Spark

- Apache spark is an open source cluster-computing framework
- real-time data processing with huge data
- originally UC Berkeley AMP lab
- later donated the Apache Software Foundation
- highly valued framework

- Map Reduce (Hadoop) has problem, by solve only batch processing, not real time
- Spark is 10 faster than Hadoop
- spark solves general purpose of cluster computing systems(real time data and batch processing)
- Hadoop written in java (class)
- Spark written in scala (less lines coding) functional programming
- Spark Core control everyting
  ontop
- Spark sql, spark streaming (quiery), MLib (machine learning), GraphX (store graphical related retrieve data)
  on top
- DataFrames is we get data (abstract)

## Compoenents

Driver (master) inside Spark Context
spark context control (instruct) Workers
Workers (Executor(Tasks))
If a task failed it rebuilts task again, That means fault tolerant.

# Abstractions

Resilient Distributed Datasets (RDD) core components, whenever operateing and data it is all RDD. Dataset which are reconstructed at nodes. if there is a failure, it is reconstructed.

- Immutable data,
- Dataframes are abstractions
- DStream are api for stream processing

# RDD

- transforming data, generating data on which
- DAG, Transformations are generated as Directed Acyclic Graph (DAG)
- DAG can be recomputed during failure (recreated)
- transformations that are happening at RDD (map, filter, flatMap, textFile, ...)
- Immutable, when it is created, you can not change it.

# Lifecycle in Spark

1. Data Source (DB, File) HDFS, S3, Cassandra
2. Transformation
3. Action (reduced, group by)
4. UI Dashboard or Processed

In other terms,

1. Load data on Cluster
2. Create RDD
3. Do Transformation
4. Perform Action
5. Create Data Frame
6. Perform Queries on Data Frame
7. Run SQL on Data Frames
