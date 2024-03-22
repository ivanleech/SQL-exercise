WITH RankedEmployees AS (
    SELECT 
        e.name AS employee,
        e.salary,
        e.departmentid,
        d.name AS department, 
        DENSE_RANK() OVER (PARTITION BY e.departmentid ORDER BY e.salary DESC) AS employee_rank
    FROM 
        employee e
    JOIN
        department d ON e.departmentId = d.id
)
SELECT 
    department,
    employee,
    salary,
    departmentId
FROM 
    RankedEmployees
WHERE 
    employee_rank <= 3;
