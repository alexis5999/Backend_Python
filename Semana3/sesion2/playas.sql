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

create table t_registro(
  reg_id int not null auto_increment primary key,
  reg_fechin datetime,
  reg_fechfin datetime,
  playa_id int,
  veh_id int,
  foreign key (playa_id) references t_playa(playa_id),
  foreign key (veh_id) references t_vehiculo(veh_id),
)

-- Insertar  datos a la tabla t_vehiculo
 insert into t_vehiculo
 (veh_placa, veh_marca, veh_anio, veh_modelo, veh_color) values
 ('A3A123','VOLKSWAGEN', 2010, 'JETTA', 'NEGRO' ),
 ('AWM047','AUDI', 2020, 'A3', 'ROJO' ),
 ('AWM045','SUSUKI', 2021, 'GRAN NOMADE', 'GRIS' ),
 ('AWM046','MAZDA', 2019, 'CX9', 'AZUL' );

-- Insertar datos a la tabla t_playa
insert into t_playa
(playa_dir, playa_cap) values
('Av. Arequipa 1234', 50 ),
('Av.Javier Prado', 200)
