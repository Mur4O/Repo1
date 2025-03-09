create or replace procedure dbo.Create_Shedule()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.Shedule;
        RAISE NOTICE 'Пересоздание таблицы dbo.Shedule';
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Новая таблица';
    end;
    begin
        create table dbo.Shedule
        (
         LessonID       serial  not null
        ,LessonDate     date    not null    constraint DF_dbo_Shedule_LessonDate default current_date
        ,IDTeacher      int     not null
        ,LessonNum      int     not null
        ,IDSubject      int     not null

        ,constraint PK_dbo_Shedule_LessonID primary key (LessonID)
        );
    end;
end;
$$;

call dbo.Create_Shedule();