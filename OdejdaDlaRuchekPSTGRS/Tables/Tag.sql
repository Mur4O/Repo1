create table dbo.Tag
(
     Id     serial      not null
    ,Title  text        not null
    ,Color  nchar(7)    not null

    ,constraint PK_dbo_Tag primary key (Id)
);