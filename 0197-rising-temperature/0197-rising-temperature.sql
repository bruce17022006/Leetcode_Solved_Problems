/* Write your PL/SQL query statement below */
select w.id as id from Weather w join Weather w1 on (w.recordDate-w1.recordDate)=1 where w.temperature > w1.temperature; 