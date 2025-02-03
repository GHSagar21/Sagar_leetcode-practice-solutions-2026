# Write your MySQL query statement below

# Using LAG and DATE_ADD Approach 
SELECT id
FROM (
    SELECT *,
           LAG(temperature) OVER (ORDER BY recordDate) AS previous_temperature,
           LAG(recordDate) OVER (ORDER BY recordDate) AS previous_date
    FROM Weather
) AS TempData
WHERE temperature > previous_temperature AND recordDate = DATE_ADD(previous_date, INTERVAL 1 DAY);

#Using JOIN and DATEDIFF

-- SELECT 
--     w1.id
-- FROM 
--     Weather w1
-- JOIN 
--     Weather w2
-- ON 
--     DATEDIFF(w1.recordDate, w2.recordDate) = 1
-- WHERE 
--     w1.temperature > w2.temperature;
