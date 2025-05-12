SET datestyle = 'ISO, DMY';

insert into dbo.Gender
(code, name)
values
('м', 'Мужчина'),
('ж', 'Женщина');

insert into dbo.tag
(title, color)
values
('Новый клиент', '#a535ab'),
('Постоянный клиент', '#37ab35');
