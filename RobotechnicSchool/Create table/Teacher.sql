create or replace procedure dbo.Create_Teacher()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.Teacher;
        RAISE NOTICE 'Пересоздание таблицы dbo.Teacher';
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Новая таблица';
    end;
    begin
        create table dbo.Teacher
        (
         ID             SERIAL      not null
        ,FIO            text        not null
        ,PasportSerie   char(4)     not null
        ,PassportNumber char(6)     not null
        ,Phone          text        not null
        ,Address        text        not null
        ,DateOfBirth    date

        ,constraint PK_dbo_Teacher_ID primary key (ID)
        );
    end;
end;
$$;

call dbo.Create_Teacher();
