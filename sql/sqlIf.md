# if statement

> IF(condition, Yes, No)
> IF(month = "Jan", revenue, Null)


# not in

```SQL
SELECT A.Name from Customers A
LEFT JOIN Orders B on  a.Id = B.CustomerId
WHERE b.CustomerId is NULL
```

```SQL
SELECT DISTINCT
	title
FROM
	Content
	INNER JOIN TVProgram ON Content.content_id = TVProgram.content_id
		AND LEFT(program_date, 7) = "2020-06"
		AND Kids_content = 'Y'
		AND content_type = 'Movies'```

```SQL
SELECT distinct title
FROM content c
JOIN tvprogram t
ON c.content_id = t.content_Id
WHERE program_Date LIKE "2020-06-%" AND kids_content = 'Y' AND content_type = 'Movies'
```

```SQL
SELECT DISTINCT c.title
FROM Content c
JOIN TVProgram p
    ON c.content_id = p.content_id
WHERE c.Kids_content = 'Y'
    AND c.content_type = 'Movies'
    AND MONTH(p.program_date) = 6
    AND YEAR(p.program_date) = 2020;
```

# Partition
add a column with count numbers or max over similar numbers
```SQL
SELECT Name,
  SECONDNAME,
  THIRDNAME,
  COUNT(*) OVER (PARTITION BY SECONDNAME)
```

# subdate
estime the difference
> subdate(current_date, 1)

# TO_DAYS
estimate the days from zero
> TO_DAYS(t1.recordDate) + 1

# DATEDIFF
estimate the difference of two times
DATEDIFF(a.Recorddate,b.Recorddate) = 1

# CASE

CASE
    WHEN Quantity > 30 THEN "The quantity is greater than 30"
    WHEN Quantity = 30 THEN "The quantity is 30"
    ELSE "The quantity is under 30"
END

# RANK() & DENSE_RANK()
RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(O.product_id) DESC) AS rnk

RANK 1, 1, 3, 4, 5 > Skip 2
DENSE 1, 1, 2, 3, 4

# ROWS
EACH ROWS ONE ENTITY IRRESPECTIVE SIMILAR VALUES
DEFAULT
> AVG(Salary) OVER (ORDER BY  Salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS average

ALL ROWS AT ONES
> AVG(Salary) OVER (ORDER BY  Salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS average
> SUM(Salary) OVER (ORDER BY Salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS average
> COUNT(Salary) OVER (ORDER BY Salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS average

ONE BELOW ONE OVER
> AVG(Salary) OVER (ORDER BY Salary ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS average

# RANGE
IF VALUES ARE SAME, IT BEHAVES AS ONE ENTITY
> AVG(Salary) OVER (ORDER BY  Salary RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS average

# LAST_VALUE()
> LAST_VALUE(Salary) OVER (ORDER BY  Salary RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS average
> LAST_VALUE(Salary) OVER (ORDER BY  Salary RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS average

# CHOOSE
CHOOSE(1,"SMT1", "SMT2")

# GROUP_CONCAT

>SELECT sell_date, COUNT(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date

# DATE_FORMAT

> DATE_FORMAT(date,'%Y%m')

# SUBSTR
'2020-02'
>substr(order_date, 6, 2) = 2

# LEFT
>Left(order_date, 7) = '2020-02'
