create or replace procedure dbo.Create_TeacherToSubject()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.TeacherToSubject;
        RAISE NOTICE 'Пересоздание таблицы dbo.TeacherToSubject';
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Новая таблица';
    end;
    begin
        create table dbo.TeacherToSubject
        (
         IDTeacher      int      not null
        ,

        ,constraint PK_dbo_TeacherToSubject_ID primary key (ID)
        );
    end;
end;
$$;

call dbo.Create_Teacher();