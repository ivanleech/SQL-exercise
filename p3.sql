SELECT 
    c.customer_name,
    c.city,
    c.grade,
    s.name AS Salesman,
    o.ord_no,
    o.ord_date,
    o.purch_amt
FROM 
    customer c
LEFT JOIN 
    orders o ON c.customer_id = o.customer_id
LEFT JOIN 
    salesman s ON c.salesman_id = s.salesman_id
WHERE 
    -- order above 2000 and must have grade
    (o.purch_amt >= 2000 AND c.grade IS NOT NULL)
    -- or have not placed any order 
    OR o.ord_no IS NULL
ORDER BY 
    c.customer_name, o.ord_no;
