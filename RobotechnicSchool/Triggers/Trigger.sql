-- Создаём триггерную функцию
CREATE OR REPLACE FUNCTION trg_after_insert_shedule()
RETURNS TRIGGER AS
$$
BEGIN
    -- Вставляем записи в Attendance для всех студентов
    INSERT INTO dbo.Attendance (LessonID, StudentID, Availability, Grade)
    SELECT NEW.LessonID, s.StudentID, TRUE, NULL
    FROM dbo.Students s;  -- Предполагаем, что есть таблица dbo.Students с идентификаторами студентов

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаём триггер, который срабатывает после вставки в dbo.Shedule
CREATE TRIGGER trg_insert_shedule
AFTER INSERT ON dbo.Shedule
FOR EACH ROW
EXECUTE FUNCTION trg_after_insert_shedule();
