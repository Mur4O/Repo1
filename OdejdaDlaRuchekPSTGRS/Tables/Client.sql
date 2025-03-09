create table dbo.Client
(
     Id                 serial  not null
    ,FirstName          text    not null
    ,LastName           text    not null
    ,Patronymic         text
    ,Birthday           date
    ,RegistrationDate   date    not null    constraint DF_dbo_Client__RegistrationDate default current_timestamp
    ,Email              text    not null
    ,Phone              int     not null
    ,GenderCode         int     not null
    ,PhotoPath          text

    ,constraint PK_dbo_Client primary key (Id)
);