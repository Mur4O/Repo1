SELECT
    tc.table_name
    ,tc.constraint_name
FROM information_schema.table_constraints AS tc
WHERE tc.constraint_type = 'FOREIGN KEY';