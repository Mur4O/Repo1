create table dbo.Gender
(
     Code   nchar(1)    not null
    ,Name   text        not null

    ,constraint PK_dbo_Gender primary key (Code)
);