create or replace procedure dbo.Create_dbo()
LANGUAGE plpgsql
AS
$$
begin
        create schema dbo;
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Схема уже существует';
end;
$$;

call dbo.Create_dbo();