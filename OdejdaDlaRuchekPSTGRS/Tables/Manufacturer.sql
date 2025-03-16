create table dbo.Manufacturer
(
    Id          serial  not null
    ,Name       text    not null
    ,StartDate  date    not null

    ,constraint PK_dbo_Manufacturer primary key (Id)
);