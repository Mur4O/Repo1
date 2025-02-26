select
from information_schema.constraint_table_usage
where
    constraint_schema = 'dbo'
    and constraint_name like 'pk%'