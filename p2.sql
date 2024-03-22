WITH agg AS (
    SELECT stock_name,
        operation,
        SUM(price) AS price
    FROM stock
    GROUP BY stock_name,
        operation
)

SELECT stock_name,
    SUM(
        CASE
            WHEN operation = 'sell' THEN price
            ELSE -price
        END
    ) AS capital_gain_loss
FROM agg
GROUP BY stock_name;