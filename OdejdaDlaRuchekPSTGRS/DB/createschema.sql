do
$$
begin
if (select schema_name from information_schema.schemata where schema_name = 'dbo') is null then
    create schema dbo;
end if;
end;
$$;