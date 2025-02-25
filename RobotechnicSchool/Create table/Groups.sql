create or replace procedure dbo.Create_Groups()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.Groups;
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Пересоздание таблицы dbo.Groups';
    end;
    begin
        create table dbo.Groups
        (
         Name           text        not null

        ,constraint PK_dbo_Groups_Name primary key (Name)
        );
    end;
end;
$$;

call dbo.Create_Groups();