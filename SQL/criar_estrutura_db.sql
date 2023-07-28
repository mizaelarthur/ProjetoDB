CREATE TABLE cargo(
    id_cargo    SERIAL,
    cargo  VARCHAR(255),
    CONSTRAINT pk_id_cargo PRIMARY KEY (id_cargo),
    CONSTRAINT un_cargo UNIQUE(cargo)
);


CREATE TABLE funcao(
    id_funcao   SERIAL,
    funcao VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_funcao PRIMARY KEY (id_funcao),
    CONSTRAINT un_funcao UNIQUE(funcao)
);


