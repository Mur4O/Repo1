create or replace procedure dbo.Create_Student()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.Student;
        RAISE NOTICE 'Пересоздание таблицы dbo.Student';
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Новая таблица';
    end;
    begin
        create table dbo.Student
        (
         ID             SERIAL      not null
        ,FIO            text        not null
        ,PasportSerie   char(4)     not null
        ,PassportNumber char(6)     not null
        ,Phone          text        not null
        ,Address        text        not null
        ,DateOfBirth    date

        ,constraint PK_dbo_Student_ID primary key (ID)
        );
    end;
end;
$$;

call dbo.Create_Student();