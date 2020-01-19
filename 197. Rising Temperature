select 
    a.Id as Id
    from 
    Weather as a join
    Weather  as b on datediff(a.RecordDate, b.RecordDate) = 1 and  
    a.Temperature > b.Temperature ;
