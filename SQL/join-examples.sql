SELECT st.name, sa.total
FROM stores st
    INNER JOIN sales sa 
    ON sa.store = st.store
WHERE st.store_status = 'A'
LIMIT 10;

/* What is the average liter size by store?  */
SELECT ROUND(AVG(sa.liter_size)) AS "Avg Liter Size", st.name AS "Store Name"
FROM sales sa 
    JOIN stores st
    ON sa.store = st.store
GROUP BY st.store
LIMIT 10;

/* GET the dates and totals for sales at Mike's liquors */
SELECT st.name, sa.date, sa.total
FROM sales sa 
    JOIN stores st
    ON st.store = sa.store
WHERE st.name LIKE 'M%'
LIMIT 10;

/* Get the store name, category name, and proof of 
sales in Black Hawk, Adair, or Wright counties. 
Sort your results alphabetically by name and limit 
the results to 10 items. */
SELECT UPPER(st.name), LOWER(sa.category_name), pr.proof
FROM stores st
    JOIN sales sa ON sa.store = st.store
    JOIN products pr ON pr.item_no = sa.item
WHERE sa.county IN ('Black Hawk', 'Adair', 'Wright')
ORDER BY st.name ASC
LIMIT 10;


