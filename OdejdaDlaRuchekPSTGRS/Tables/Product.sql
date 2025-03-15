create table dbo.Product
(
    Id              serial          not null
    ,Title          text            not null
    ,Costs          decimal(10,2)   not null
    ,Description    text                null
    ,IsActive       boolean         not null    constraint DF_dbo_Product__IsActive default TRUE
    ,ManufacturerID int                 null
    ,CategoryID     int                 null

    ,constraint PK_dbo_Product primary key (Id)
);