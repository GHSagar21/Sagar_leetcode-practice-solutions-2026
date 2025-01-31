# Write your MySQL query statement below
select product_name, year, price
from Sales as s LEFT JOIN Product as p ON  p.product_id = s.product_id;
