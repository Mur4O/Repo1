create table dbo.Service
(
     Id serial NOT NULL
	,Title text NOT NULL
	,Cost decimal(10, 2) NOT NULL
	,DurationInStock int NOT NULL
	,Description text NULL
	,Discount float NULL
	,MainImagePath dbo.PathFile NULL
    
    ,constraint PK_dbo_Service primary key (Id)
);