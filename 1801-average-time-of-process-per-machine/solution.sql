SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a JOIN Activity b ON a.machine_id = b.machine_id AND a.process_id = b.process_id
WHERE a.activity_type = 'start' AND b.activity_type = 'end'
GROUP BY a.machine_id # GROUP BY - it groups all the values separately based on the attribute given here it is based on the machine_id
# or else it will give a single value for everything


-- SELECT a.machine_id, a.process_id, a.timestamp AS start_time, b.timestamp AS end_time, AVG(b.timestamp - a.timestamp) AS processing_time
-- FROM Activity a JOIN Activity b ON a.machine_id = b.machine_id AND a.process_id = b.process_id
-- WHERE a.activity_type = 'start' AND b.activity_type = 'end'
-- GROUP BY a.machine_id
