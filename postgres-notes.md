# Postgres notes

1. `COALESCE(expression, opt_val_if_expression_null)`
2. `LAG(aggregator_func, offset_to_shift)` shift n from current group in *group by*, *partition by* (or *order by*?) query
3. `SELECT SUM(a) OVER PARTITION BY a, b FROM A;` select attributes using aggregation functions
4. `SELECT a FILTER (WHERE ...), b FROM A;` sub filters in select attributes
5. `SELECT ... FROM A LEFT JOIN B on A.a = B.a WHERE A.c = '3';`
6. **UNION and UNION ALL**  
 UNION combines result sets and leave distinct values  
 UNION ALL allows duplicate values
7. Double quote in SQL string represents column names or table names. Postgres does not accept single quotes on column and table names.
8. Single quote in SQL string represents string value.
9. `DATE_PART('year', ma."worked_at"::date)`  add type identifier to tell function `DATE_PART` the source type

