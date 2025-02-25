create or replace procedure dbo.Create_Subjects()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.Subjects;
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Пересоздание таблицы dbo.Subjects';
    end;
    begin
        create table dbo.Subjects
        (
         ID             SERIAL      not null
        ,Name           text        not null

        ,constraint PK_dbo_Subjects_ID primary key (ID)
        );
    end;
end;
$$;

call dbo.Create_Subjects();