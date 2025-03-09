create or replace procedure dbo.Create_Attendance()
LANGUAGE plpgsql
AS
$$
begin
    begin
        drop table dbo.Attendance;
        RAISE NOTICE 'Пересоздание таблицы dbo.Attendance';
    EXCEPTION WHEN OTHERS
    then
        RAISE NOTICE 'Новая таблица';
    end;
    begin
        create table dbo.Attendance
        (
        LessonID        int         not null
        ,StudentID      int         not null
        ,Availability   boolean     not null    constraint DF_dbo_Attendance_Availability default TRUE
        ,Grade          smallint        null    check ((Grade >= 2 and Grade <= 5) or Grade is null)
        );
    end;
end;
$$;

call dbo.Create_Attendance();
