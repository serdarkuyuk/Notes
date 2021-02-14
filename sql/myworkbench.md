# MySQL community server

1) mysql.com > download
2) click MySQL Community (GPL) Downloads
3) MySQL Community Server
4) macOS 10.15 (x86, 64-bit), DMG Archive

# Installing MySQL workbench

1) https://dev.mysql.com/downloads/workbench/
2) Sign in
3) Download


in application folder double click.
if not opened, go to macos settings open security general
and allow mysql at the bottom.
Now you can run


# MySQL workbench
delete connection by right click
mySQL connection + sign

# Commands
USE tableName or double click to table

USE sql_store;

SELECT *
FROM customers;

-- comments
AND operator is execute earlier than OR

## REGEXP  
WHERE last_name REGEXP 'field'
^field begining
field$ ending
'field|mac' contains field or mac
[gim]e - ge or ie or me
[a-f]

# ORDER BY

SELECT FIRST, SECOND
FROM TABLE
ORDER BY 1, 2 (refers to columns)

# LIMIT
LIMIT 6, 3  (skip 6 and get the 3 item from 6)

## INSERT
* if there is default value, we can right default

```sql
INSERT INTO customers
VALUES (DEFAULT, 'john', 'smith',
'1990-01-01', NULL, 'address','city','CA',
DEFAULT)```

OR

```sql
INSERT INTO customers(first_name,
    birth_date,
    address,
    city,
    state)
VALUES ('john', 'smith',
'1990-01-01', 'address','city','CA')```

to enter multiple
```sql
INSERT INTO shippers (name)
VALUES ('Shippers1'), ('shipppers2'),('shipppers3')```

# INSERT PARENT-CHILD
```SQL
INSERT INTO orders (customer_id, order_date, status)
VALUES (1, "2019-01-01", 1)

INSERT INTO order_items
VALUES
    (LAST_INSERT_ID(), 1, 1, 2.95), --This is child
    (LAST_INSERT_ID(), 2, 1, 3.95)```

# COPY TABLE
```
CREATE TABLE orders_archived AS
SELECT * FROM orders
```
after truncate (deleting all the values from the table)
```sql
INSERT INTO orders_archived
SELECT * FROM orders
WHERE order_date < '2019-01-01'```

# UPDATE

```sql
UPDATE invoice
SET payment_total = 10, payment_date = Null
WHERE invoice_id = 1
```
```sql
UPDATE invoice
SET payment_total = invoice_total *0.5,
    payment_date = due_date
WHERE invoice_id = 1
```
# DELETE
```SQL
DELETE FROM invoices
WHERE invoice_id =(
        SELECT *
        FROM client
        WHERE name = 'Myworks'
)
```

```sql
use mytestdb;
drop table if exists country ;
create table country(country_id int NOT NULL AUTO_INCREMENT primary key, country_name varchar(50), last_update datetime NOT NULL);
```

## Set local file readible
show global variables like 'local_infile';
set global local_infile=true;


## set local file readabile
Go to the MySQL Connections page.
Right click the connection and click 'Edit connection'.
Select 'Advanced' option. Paste the below line in the 'Others' box.
OPT_LOCAL_INFILE=1
Click 'Test Connection'. It will successfully update the connection.
OPT_LOCAL_INFILE=1
