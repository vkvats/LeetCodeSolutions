select 
    ifnull(
        (select distinct Salary 
           from Employee 
           order by Salary DESC 
           limit 1, 1), 
        NULL) as SecondHighestSalary;
