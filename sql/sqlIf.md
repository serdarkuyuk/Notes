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
