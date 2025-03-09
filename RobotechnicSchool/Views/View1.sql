CREATE OR REPLACE VIEW dbo.v_Shedule AS
SELECT
    s.LessonID,
    s.LessonDate,
    t.FIO AS TeacherName,
    s.LessonNum,
    sub.Name AS SubjectName
FROM dbo.Shedule s
JOIN dbo.Teacher t ON s.IDTeacher = t.ID
JOIN dbo.Subjects sub ON s.IDSubject = sub.ID;

select * from dbo.v_Shedule