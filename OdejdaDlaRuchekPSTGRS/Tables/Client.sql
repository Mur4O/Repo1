create table dbo.Client
(
     Id                 serial      not null
    ,FirstName          text        not null
    ,LastName           text        not null
    ,Patronymic         text            null
    ,Birthday           date            null
    ,RegistrationDate   date        not null    constraint DF_dbo_Client__RegistrationDate default current_timestamp
    ,Email              text        not null
    ,Phone              int         not null
    ,GenderCode         nchar(1)    not null
    ,PhotoPath          text            null

    ,constraint PK_dbo_Client primary key (Id)
);