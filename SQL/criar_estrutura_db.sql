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


CREATE TABLE categoria(
    id_categoria    SERIAL,
    categoria  VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_categoria PRIMARY KEY (id_categoria),
    CONSTRAINT un_categoria UNIQUE(categoria)
);



CREATE TABLE jornada_trabalho(
    id_jornada  SERIAL,
    jornada     VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_jornada PRIMARY KEY (id_jornada),
    CONSTRAINT un_jornada UNIQUE(jornada)
);


CREATE TABLE campus(
    id_campus     SERIAL,
    campus   VARCHAR(10) NOT NULL,
    CONSTRAINT pk_id_campus PRIMARY KEY (id_campus),
    CONSTRAINT un_campus UNIQUE(campus)
);


CREATE TABLE setor_siape(
    id_setor    SERIAL,
    setor_siape  VARCHAR(15) DEFAULT '------' NOT NULL,
    CONSTRAINT pk_id_setor PRIMARY KEY (id_setor),
    CONSTRAINT un_setor_siape UNIQUE(setor_siape)
);


CREATE TABLE setor_suap(
    id_setor_suap   SERIAL,
    setor_suap VARCHAR(15) DEFAULT '------' NOT NULL,
    CONSTRAINT pk_id_setor_suap PRIMARY KEY (id_setor_suap),
    CONSTRAINT un_setor_suap UNIQUE(setor_suap)
);


