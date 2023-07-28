CREATE TABLE cargo(
    id_cargo    SERIAL,
    nome_cargo  VARCHAR(255),
    CONSTRAINT pk_id_cargo PRIMARY KEY (id_cargo),
    CONSTRAINT un_nome_cargo UNIQUE(nome_cargo)
);


CREATE TABLE funcao(
    id_funcao   SERIAL,
    nome_funcao VARCHAR(255) DEFAULT '------' NOT NULL,
    CONSTRAINT pk_id_funcao PRIMARY KEY (id_funcao),
    CONSTRAINT un_nome_funcao UNIQUE(nome_funcao)
);

CREATE TABLE categoria(
    id_categoria    SERIAL,
    nome_categoria  VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_categoria PRIMARY KEY (id_categoria),
    CONSTRAINT un_nome_categoria UNIQUE(nome_categoria)
);
