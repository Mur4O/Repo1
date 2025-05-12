create table dbo.ClientService
(
     Id         serial      not null
    ,ClientId   int         not null
    ,ServiceId  int         not null
    ,StartTime  timestamp
    ,Comment    text

    ,constraint PK_dbo_ClientService primary key (Id)
);
