CREATE TABLE cargo(
    id_cargo    SERIAL,
    nome_cargo  VARCHAR(255),
    CONSTRAINT pk_id_cargo PRIMARY KEY (id_cargo),
    CONSTRAINT un_nome_cargo UNIQUE(nome_cargo)
);
