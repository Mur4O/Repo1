### Задача 1

Напишите запрос для получения фамилий сотрудников, содержащих более одной буквы "о".

```SQL
CREATE TABLE Employee 
(
Id int IDENTITY(1,1) Primary key not null,
FirstName nvarchar(50) not null,
LastName nvarchar(50) not null,
Patronymic nvarchar(50),
Birthday date,
Email nvarchar(255),
Phone nvarchar(20) not null,
GenderCode nchar(1) not null
);

SELECT e.LastName
FROM Employee e
WHERE PATINDEX('%o%o%', e.LastName) <> 0
```

### Задача 2

Напишите скрипт для получения списка клиентов, чей день рождения наступит завтра.

```SQL
CREATE TABLE Client
(
Id int IDENTITY(1,1) Primary key not null,
FirstName nvarchar(50) not null,
LastName nvarchar(50) not null,
Birthday date,
Email nvarchar(255),
Phone nvarchar(20) not null,
GenderCode nchar(1) not null
);


SELECT c.Id, c.FirstName, c.LastName, c.Birthday
FROM Client c
WHERE DAY(c.Birthday) = DAY(DATEADD("d", 1 ,GETDATE())) AND MONTH(c.Birthday) = MONTH(DATEADD("d", 1 ,GETDATE()))
```

### Задача 3

Напишите скрипт для получения списка сотрудников, имеющих сумму продаж, превышающую 1млн рублей за январь 2015 года.

```SQL
CREATE TABLE Employee 
(
Id int IDENTITY(1,1) Primary key not null,
FirstName nvarchar(50) not null,
LastName nvarchar(50) not null,
Patronymic nvarchar(50),
Birthday date,
Email nvarchar(255),
Phone nvarchar(20) not null,
GenderCode nchar(1) not null
);

CREATE TABLE Sales
(
Id int IDENTITY(1,1) Primary key not null,
Costs decimal(10, 2) not null,
IdEmp int NOT NULL,
DateOfSale datetime NOT NULL DEFAULT GETDATE(), 
FOREIGN KEY (IdEmp) REFERENCES Employee(Id)
);

SELECT e. Id, e.FirstName, e.LastName 
FROM Sales s JOIN Employee e ON s.IdEmp = e.Id 
WHERE s.DateOfSale BETWEEN '2015-01-01' AND '2015-01-31' 
GROUP BY e.Id, e.FirstName, e.LastName 
HAVING SUM(s.Costs) > 1000000
```

### Задача 4

Напишите скрипт для получения количества уникальных клиентов для каждого менеджера.

```SQL
CREATE TABLE Client
(
Id int IDENTITY(1,1) Primary key not null,
FirstName nvarchar(50) not null,
LastName nvarchar(50) not null,
Birthday date,
Email nvarchar(255),
Phone nvarchar(20) not null,
GenderCode nchar(1) not null
)

CREATE TABLE Manager
(
Id int IDENTITY(1,1) Primary key not null,
FirstName nvarchar(50) not null,
LastName nvarchar(50) not null,
Patronymic nvarchar(50),
Birthday date,
Email nvarchar(255),
Phone nvarchar(20) not null,
GenderCode nchar(1) not null
)

CREATE TABLE ManagerToClient
(
IdPair int IDENTITY(1,1) Primary key not null,
IdManager int not null,
IdClient int not null,
FOREIGN KEY (IdManager) REFERENCES Manager(Id),
FOREIGN KEY (IdClient) REFERENCES Client(Id)
);

SELECT mtc.IdManager, COUNT(DISTINCT mtc.IdClient) NumOfUniqueCustomers
FROM ManagerToClient mtc
GROUP BY mtc.IdManager
```

### Задача 5

Напишите скрипт для получения списка клиентов, не совершивших ни одного заказа за прошедшие пол года (180 дней от текущей даты).

```SQL
CREATE TABLE Client
(
Id int IDENTITY(1,1) Primary key not null,
FirstName nvarchar(50) not null,
LastName nvarchar(50) not null,
Birthday date,
Email nvarchar(255),
Phone nvarchar(20) not null,
GenderCode nchar(1) not null
);

CREATE TABLE [Order]
(
Id int IDENTITY(1,1) Primary key not null,
Costs decimal(10, 2) not null,
OrderDate date NOT NULL DEFAULT GETDATE(),
IdClient int not null,
FOREIGN KEY (IdClient) REFERENCES Client(Id)
);

with cte1 as (
SELECT COUNT(o.Id) Orders, o.IdClient 
FROM [Order] o 
WHERE DATEDIFF(DAY, o.DateOfSale, GETDATE()) <= 180 
GROUP BY o. IdClient)

SELECT c.Id, c.FirstName, c.LastName 
FROM Client c LEFT JOIN cte1 c1 ON c1.IdClient = c.Id 
WHERE c1.IdClient IS NULL
```

### Задача 6

Напишите скрипт для получения количества заказов за 21.01.2015 г. При этом на таблице существует следующий индекс:  
create index IX_dbo_Order__OrderDate on dbo.Order (Order_Date)

```SQL
CREATE TABLE [Order]
(
Id int IDENTITY(1,1) Primary key not null,
Costs decimal(10, 2) not null,
OrderDate date NOT NULL DEFAULT GETDATE(),
IdClient int not null,
FOREIGN KEY (IdClient) REFERENCES Client(Id)
);

CREATE INDEX IX_dbo_Order_OrderDate on dbo.[Order](OrderDate);


SELECT COUNT(o.Id) CntdOrders
FROM [Order] o
WHERE o.OrderDate = '2015-01-21'
```

### Задача 8

Напишите процедуру поиска сотрудника по любой комбинации параметров (Fam, Tel, TabNom). Процедура возвращает все поля из таблицы «Сотрудники». При этом на таблице существуют следующий индексы:  
```SQL
create index IX_dbo_Employee__Fam on dbo.Employee (Fam)  
create index IX_ dbo_Employee__Tel on dbo.Employee (Tel)  
create index IX_ dbo_Employee__TabNom on dbo.Employee (TabNom)
```

```SQL
CREATE TABLE Employee
(
Id int IDENTITY(1,1) Primary key not null,
[Fam] nvarchar(50),
[Tel] nvarchar(20),
[TabNom] nvarchar(50)
);

create index IX_dbo_Employee__Fam on dbo.Employee (Fam);
create index IX_dbo_Employee__Tel on dbo.Employee (Tel);
create index IX_dbo_Employee__TabNom on dbo.Employee (TabNom);


CREATE PROCEDURE FindEmployee
	@Fam nvarchar(50) = NULL,
	@Tel nvarchar(20) = NULL,
	@TabNom nvarchar(50) = NULL
AS
	SELECT * 
	FROM Employee 
	WHERE (@Fam IS NULL OR [Fam] = @Fam) 
		AND (@Tel IS NULL OR [Tel] = @Tel)
		AND (@TabNom IS NULL OR [TabNom] = @TabNom);


EXEC FindEmployee --@Fam = 'A', @Tel = '1'
```

### Задача 10

Для каждого календарного дня в прошлом месяце, включая и дни без продаж, выведите количество заказов и общую сумму в таком виде:
```
|-------------------------------------------|
| Дата     | Количество заказов | Сумма     |
|----------|--------------------|-----------|
| 01.01.01 | 0                  | 0         |
| 02.01.01 | 0                  | 0         |
| 03.01.01 | 200                | 20700     |
| 04.01.03 | 453                | 434900,34 |
|-------------------------------------------|
```

```SQL
with cte as (
	SELECT * FROM (VALUES (1), (2), (3), (4), (5), (6)) as t(id)),

cte2 as (
--Данный скрипт выводит таблицу с одним столбцом, заполненным датами прошлого месяца, начиная с первого числа и заканчивая последним днём месяца.
SELECT
	DATEADD(DAY, ROW_NUMBER() OVER (Order by c.id), DATEADD(DAY, -DAY(GETDATE()) ,DATEADD(MONTH, -1, CAST(GETDATE() as date)))) PastMonth
FROM cte c CROSS JOIN cte c1)


SELECT PastMonth Дата, COUNT(ALL s.Client) Количество_заказов, ISNULL(SUM(s.Costs), 0) Сумма
FROM cte2 LEFT JOIN Sales s ON s.SaleDate = PastMonth
WHERE MONTH(PastMonth) = MONTH(DATEADD(MONTH, -1, GETDATE()))
GROUP BY PastMonth
```

### Задача 11

Задана иерархия, в которой имеется два типа узлов: пустые и полные. Напишите скрипт для получения дочерних элементов следующего уровня для заданного узла иерархии, но только имеющих хотя бы одного «полного» потомка на любом из уровней. Пример (рис.): Для Узла А надо вывести С и D, т.к. С - имеет заполненный узел на одном из дочерних уровней, а D - сам является заполненным. В - не является заполненным и не имеет заполненных наследников, поэтому его выводить не надо.

```SQL
CREATE TABLE Hierarchy
(
ID int Primary Key,
Code int,
[Name] nvarchar(50),
Parent_ID int,
IsFull int
)

INSERT INTO Hierarchy VALUES
(1,1,'A',NULL,0),
(2,2,'B',1,0),
(3,3,'C',1,1),
(4,4,'D',2,0),
(5,5,'E',2,0),
(6,6,'F',2,1),
(7,7,'G',4,0),
(8,8,'H',4,0),
(9,9,'I',5,0),
(10,10,'J',6,1),
(11,11,'K',7,0),
(12,12,'L',9,1),
(13,13,'M',10,0),
(14,14,'N',10,0);
--Каждому узлу графа присвоил буквенное имя

CREATE PROCEDURE FindElements
	@Node nvarchar(1)
AS
	SELECT DISTINCT h1.[Name]
	FROM Hierarchy h 
		LEFT JOIN Hierarchy h1 ON h.ID = h1.Parent_ID
		LEFT JOIN Hierarchy h2 ON h1.ID = h2.Parent_ID
		LEFT JOIN Hierarchy h3 ON h2.ID = h3.Parent_ID
		LEFT JOIN Hierarchy h4 ON h3.ID = h4.Parent_ID
	WHERE h.[Name] = @Node AND (h1.IsFull = 1 OR h2.IsFull = 1 OR h3.IsFull = 1 OR h4.IsFull = 1);

EXEC FindElements @Node = 'B'
```
Схема созданного графа:
![alt text](https://github.com/Mur4O/Repo1/blob/b102575e38d25ede89417fc87b2517c06f62e672/%D0%98%D0%BB%D0%BB%D1%8E%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%BB%D1%8F%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%2011.png?raw=true)