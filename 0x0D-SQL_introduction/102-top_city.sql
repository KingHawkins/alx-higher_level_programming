-- top city by temperature in months of july to august
SELECT city, avg(value) as avg_temp FROM temperatures WHERE month > 6 && month < 9 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
