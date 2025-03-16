create table dbo.ProductSale
(
    Id                  serial      not null
    ,SateDate           timestamp   not null    constraint DF_dbo_ProductSale__SateDate default current_timestamp
    ,ProductId          int         not null
    ,Quantity           int         not null
    ,ClientServiceId    int         not null

    ,constraint PK_dbo_ProductSale primary key (Id)
);