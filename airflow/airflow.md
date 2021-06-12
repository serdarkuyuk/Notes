notes on airflow application
https://www.youtube.com/watch?v=43wHwwZhJMo&list=PLYizQ5FvN6pvIOcOd6dFZu3lQqc6zBGp2&index=4

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

DAG - directed acyclic graph
different task

1. open folder
2. cd airflow-tutorial
3. git clone https://github.com/tuanavu/airflow-tutorial.git

### run code

4. docker-compose up -d

### build code

5. docker-compose up -d --build
   5a. http://localhost:8080

### stop server

6. docker-compose down

### check which servers running

7. docker container ls

dag file - python script
step 1. importing module
setp 2. default arguments
step 3. instantiate a DAG
step 4. Tasks
step 5. Setting up Dependencies

pip install apache-airflow

```python
default_args = {
    'owner': 'airflow',
    'depends_on_past': False, #if True current task rely on previous task
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['airflow@example.com'], # notification emails
    'email_on_failure': False, # emails if it failure
    'email_on_retry': False, # emails if try happens
    'retries': 1, # if faile happens how many time try
    'retry_delay': timedelta(minutes=5), # consequtive task trials
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1), # last day to execute
}

dag = DAG(
    'example_twitter_dag', default_args=default_args,
    schedule_interval="@daily")

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t1.doc_md = """\
#### Task Documentation
You can document your task using the attributes `doc_md` (markdown),
`doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
rendered in the UI's Task Instance Details page.
![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
"""

dag.doc_md = __doc__

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)

templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag,
)

t1 >> [t2, t3]
```
