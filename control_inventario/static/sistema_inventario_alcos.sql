CREATE DATABASE sistema_alcos ;
use sistema_alcos ;

Create table Bodega
(
Id_Bodega_PK int not null auto_increment,
Nombre varchar (50) not null,
Descripción varchar (50),
PRIMARY KEY (Id_Bodega_PK)
);

Create table Categoria
(
Id_Categoria_PK int not null auto_increment,
Nombre varchar (50) not null,
Descripción varchar (50) not null,
PRIMARY KEY (Id_Categoria_PK)
);

Create table Marca
(
Id_Marca_PK int not null auto_increment,
Nombre varchar (50) not null,
PRIMARY KEY (Id_Marca_PK)
);

Create table Unidad_Medida
(
Id_Unidad_PK int not null auto_increment,
Nombre varchar (50) not null,
Medida decimal (25,2) not null,
PRIMARY KEY (Id_Unidad_PK)
);

Create table Rol_Persona
(
Id_Rol_PK int not null auto_increment,
Cargo varchar (50) not null,
PRIMARY KEY (Id_Rol_PK)
);

Create table Ingreso_Cabecera
(
Id_Ingreso_PK int not null auto_increment,
Codigo varchar (50) not null,
Descripcion varchar (50),
PRIMARY KEY (Id_Ingreso_PK)
);

Create table Egreso_Cabecera
(
Id_Egreso_PK int not null auto_increment,
Codigo varchar (50) not null,
Descripcion varchar (50),
PRIMARY KEY (Id_Egreso_PK)
);

Create table Persona
(
Id_Persona_PK varchar (50) not null,
Id_Rol_FK int not null,
Nombre varchar (50) not null,
Apellido varchar (50) not null,
Direccion varchar (50)not null,
Celular varchar (50) not null,
Correo varchar (50) not null,
PRIMARY KEY (Id_Persona_PK),
Foreign Key (Id_Rol_FK) references Rol_Persona(Id_Rol_PK)
);

Create table Producto
(
Id_Producto_PK varchar (50) not null,
Id_Marca_FK int not null,
Id_Persona_FK varchar (50) not null,
Id_Unidad_FK int not null,
Id_Categoria_FK int not null,
Nombre varchar (50) not null,
Descripcion varchar (50) not null,
PRIMARY KEY (Id_Producto_PK),
Foreign Key (Id_Marca_FK) references Marca (Id_Marca_PK),
Foreign Key (Id_Persona_FK) references Persona (Id_Persona_PK),
Foreign Key (Id_Unidad_FK) references Unidad_Medida (Id_Unidad_PK),
Foreign Key (Id_Categoria_FK) references Categoria (Id_Categoria_PK)
);

Create table Devolución
(
Id_Devolucion_PK int primary key not null auto_increment,
Detalle varchar (50) not null,
Id_Producto_FK varchar (50) not null,
fecha_hora datetime,
Foreign Key (Id_Producto_FK) references Producto(Id_Producto_PK)
);

Create table Stock
(
Id_Stock_PK int primary key not null auto_increment,
Limite varchar (50) not null,
Cantidad int not null,
Producto_FK varchar (50) not null,
Foreign Key (Producto_FK) references Producto (Id_Producto_PK)
);

Create table Proveedor
(
Id_Proveedor_PK varchar (50) primary key not null,
Id_Producto_FK varchar (50) not null,
Nombre varchar (50) not null,
Apellido varchar (50) not null,
Direccion varchar (50),
Celular varchar (50) not null, 
Correo varchar (50) not null,
Foreign Key (Id_Producto_FK) references Producto (Id_Producto_PK)
);


Create table Bodega_Producto
(
IdBod_Pro_PK int primary key not null auto_increment,
Id_Producto_FK varchar (50) not null,
Id_Bodega_FK int not null,
Cantidad int not null,
Unidad varchar (50),
fecha_hora datetime,
Foreign Key (Id_Producto_FK) references Producto (Id_Producto_PK),
Foreign Key (Id_Bodega_FK) references Bodega (Id_Bodega_PK)
);


Create table Egreso_Detalle
(
Id_Egreso_det_PK int primary key auto_increment not null,
Id_Egreso_FK int not null,
Id_Producto_FK varchar (50) not null,
Cantidad int not null,
Precio decimal (4,2) not null,
fecha_hora datetime,
Foreign Key (Id_Producto_FK) references Producto (Id_Producto_PK),
Foreign Key (Id_Egreso_FK) references Egreso_Cabecera(Id_Egreso_PK)
);

Create table Ingreso_Detalle
(
Id_Ingreso_det_PK int primary key not null auto_increment,
Id_Ingreso_FK int not null,
Id_Producto_FK varchar (50) not null,
Cantidad int not null,
Precio decimal (4,2) not null,
fecha_hora datetime,
Foreign Key (Id_Producto_FK) references Producto(Id_Producto_PK),
Foreign Key (Id_Ingreso_FK) references Ingreso_Cabecera (Id_Ingreso_PK)
);