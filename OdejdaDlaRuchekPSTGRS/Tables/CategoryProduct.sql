create table dbo.CategoryProduct
(
     Id     serial  not null
    ,Title  text    not null

    ,constraint PK_dbo_CategoryProduct primary key (Id)
);