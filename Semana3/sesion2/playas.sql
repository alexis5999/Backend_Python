-- Creación de la tabla playa en la BD MYSQL
CREATE DATABASE PLAYA;

create table t_vehiculo(
   veh_id int not null auto_increment;
   veh_placa varchar(6),
   veh_marca varchar(30),
   veh_anio year,
   veh_modelo varchar(40),
   veh_color varchar(20),
   primary key (veh_id)
);

create table t_playa(
 playa_id int not null auto_increment primary key,
 playa_dir varchar(100),
 playa_cap int
);