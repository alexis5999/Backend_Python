-- vamos a crear una bd en la cual vamos a guardar los productos y sus categorias
CREATE DATABASE minimarket;
use minimarket;
create table t_categorias(
	cat_id int not null auto_increment primary key,
    cat_desc varchar(50)
);
create table t_productos(
	prod_id int not null auto_increment primary key,
    prod_desc varchar(50),
    prod_prec decimal(5,2),
    cat_id int,
    foreign key (cat_id) references t_categorias(cat_id)
);
