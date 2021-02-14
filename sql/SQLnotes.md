
# 1. Normal Form
1NF rule #1: each column has one and only one fact (one fact in one place)
- Split it into two columns.
1NF rule #2: Each record is unique and can be identified by a primary key
- choose sth as the primary key.
1NF rule #3: no repeating groups or duplicate fields
- Split the smaller repeating group.
- Work on the largest repeating group first.
- Split the main table into two tables.

# 2. Normal Form
2NF rule #1: It must be in First Normal Form
2NF rule #2:
* No part of the primary key can determine any non-key columns where “non-key” means “not primary key”
* All non-key columns depend on the whole primary key
* Whole PK -> all non-key columns (-> read as determines)
Violation = Part of PK -> some non-key columns

1NF Tables with a single-column key do not violate the second rule of the Second Normal Form because its primary key is the whole key, which doesn’t have separate parts or columns, and determines all the non-key columns.

# 3. Normal Form
Rule #1: It must be in Second Normal Form.
Rule #2:
* The determinant of a non-key column is the primary key.
* No non-key column depends upon another.
* The primary key is the only determinant.

Violation = non-key column(s) -> other non-key column(s)
Violation = Part of PK + non-key -> other non-key column(s)
