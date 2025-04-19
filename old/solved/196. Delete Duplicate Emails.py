# Write your MySQL query statement below
delete P1.* 
    from Person as P1,
    Person as P2
    where P1.Email =P2.Email and P1.Id > P2.Id;
