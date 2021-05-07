-- Banco de Dados MySQL que alimenta a API 

-- DDL: Definição do banco de dados
-- Criação de tabelas
create database bd_imobiliaria;

use bd_imobiliaria;

create table tb_imobiliaria(
cd_imobiliaria int not null primary key auto_increment,
nome varchar(100),
endereco varchar(200)
);

create table tb_imovel(
cd_imovel int not null primary key auto_increment,
nome varchar(100),
endereco varchar(200),
descricao varchar(500),
status_ char(1),
tipo char(1),
finalidade char(1),
nr_quarto int,
nr_sala int,
nr_banheiro int, 
nr_vaga int,
cd_imobiliaria int
);

-- Criação de relacionamentos
alter table tb_imovel
add constraint fk_imobiliaria foreign key(cd_imobiliaria)
references tb_imobiliaria (cd_imobiliaria);

-- DML
-- Inserção de teste
insert into tb_imobiliaria(cd_imobiliaria, nome, endereco)
values (123, "Imobiliaria São Jorge", "Rua Cônego Walmor Castro, Ponta das Canas, Florianópolis-SC");

insert into tb_imovel(nome, endereco, descricao, status_ , tipo, finalidade,
nr_quarto, nr_sala, nr_banheiro, nr_vaga, cd_imobiliaria)
values ("Santana's Home", "Rua Tiradentes, Centro, Florianópolis-SC", "Uma casa confortável e ideal para
familias grandes", "A", "C", "R", 4, 2, 5, 3, 123);

select tb_imobiliaria.nome as nome_imobiliaria, tb_imovel.nome as nome_imovel
 from tb_imobiliaria inner join tb_imovel on tb_imovel.cd_imobiliaria = tb_imobiliaria.cd_imobiliaria;
-- DML
-- Consultas de teste
select * from tb_imovel;

select * from tb_imobiliaria; 

-- delete from tb_imovel where ;
delete from tb_imobiliaria where cd_imobiliaria = 1;

update tb_imobiliaria set nome = "Imobiliaria São Pedro", endereco = "Ceilandia, Ponta das Canas, Florianópolis-SC" where cd_imobiliaria = 123;
select * from tb_imovel where cd_imobiliaria = 1;

select * from tb_imobiliaria where nome like '%bili%';

drop table tb_imobiliaria;

delete from tb_imovel where cd_imobiliaria = 345;

-- Criação de Stored Procedure
-- Para cadastrar o usuário
DELIMITER $$

CREATE PROCEDURE FiltroImobi(in var_nome varchar(100))
BEGIN
    select * from tb_imobiliaria where nome like concat('%', var_nome, '%');
END$$

DELIMITER ;

call FiltroImobi("bili");