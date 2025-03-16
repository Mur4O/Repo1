alter table dbo.product
add constraint FK_dbo_Product__dbo_CategoryProduct foreign key (categoryid) references dbo.categoryproduct (id);

alter table dbo.product
add constraint FK_dbo_Product__dbo_Manufacturer foreign key (manufacturerid) references dbo.manufacturer (id);

alter table dbo.productsale
add constraint FK_dbo_ProductSale__dbo_Product foreign key (ProductId) references dbo.product (id);

alter table dbo.productphoto
add constraint FK_dbo_ProductPhoto__dbo_Product foreign key (productid) references dbo.product (id);

alter table dbo.tagofclient
add constraint FK_dbo_TagOfClient__dbo_Tag foreign key (tagid) references dbo.tag (id);

alter table dbo.tagofclient
add constraint FK_dbo_TagOfClient__dbo_Clietn foreign key (clientid) references dbo.client (id);

alter table dbo.client
add constraint FK_dbo_Client__dbo_Gender foreign key (GenderCode) references dbo.gender (code);

alter table dbo.clientservice
add constraint FK_dbo_ClientService__dbo_Client foreign key (clientid) references dbo.client (Id);

alter table dbo.clientservice
add constraint FK_dbo_ClientService__dbo_Service foreign key (serviceid) references dbo.service (id);

alter table dbo.servicephoto
add constraint FK_dbo_ServicePhoto__dbo_Service foreign key (serviceid) references dbo.service (id);