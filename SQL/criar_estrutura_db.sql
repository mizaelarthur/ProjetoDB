CREATE TABLE cargo(
    id_cargo    SERIAL,
    ncargo  VARCHAR(255),
    CONSTRAINT pk_id_cargo PRIMARY KEY (id_cargo),
    CONSTRAINT un_ncargo UNIQUE(ncargo)
);

CREATE TABLE setor_suap(
    id_setor_suap   SERIAL,
    nsetor_suap VARCHAR(15) DEFAULT 'nenhum' NOT NULL,
    CONSTRAINT pk_id_setor_suap PRIMARY KEY (id_setor_suap),
    CONSTRAINT un_nsetor_suap UNIQUE(nsetor_suap)
);


CREATE TABLE campus(
    id_campus     SERIAL,
    ncampus   VARCHAR(10) NOT NULL,
    CONSTRAINT pk_id_campus PRIMARY KEY (id_campus),
    CONSTRAINT un_ncampus UNIQUE(ncampus)
);

CREATE TABLE jornada_trabalho(
    id_jornada  SERIAL,
    jornada     VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_jornada PRIMARY KEY (id_jornada),
    CONSTRAINT un_jornada UNIQUE(jornada)
);

CREATE TABLE setor_siape(
    id_setor    SERIAL,
    nsetor  VARCHAR(15) DEFAULT 'nenhum' NOT NULL,
    CONSTRAINT pk_id_setor PRIMARY KEY (id_setor),
    CONSTRAINT un_nsetor UNIQUE(nsetor)
);

CREATE TABLE disciplina_ingresso(
    id_disciplina   SERIAL,
    ndisciplina VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_disciplina PRIMARY KEY (id_disciplina),
    CONSTRAINT un_ndisciplina UNIQUE(ndisciplina)
);

CREATE TABLE funcao(
    id_funcao   SERIAL,
    nfuncao VARCHAR(255) DEFAULT 'nenhum' NOT NULL,
    CONSTRAINT pk_id_funcao PRIMARY KEY (id_funcao),
    CONSTRAINT un_nfuncao UNIQUE(nfuncao)
);

CREATE TABLE categoria(
    id_categoria    SERIAL,
    ncategoria  VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_categoria PRIMARY KEY (id_categoria),
    CONSTRAINT un_ncategoria UNIQUE(ncategoria)
);

CREATE TABLE servidor(
    matricula_servidor  BIGINT NOT NULL,
    nome                VARCHAR(255) NOT NULL,
    link_fotos          VARCHAR(255) DEFAULT '------' NOT NULL,
    link_lattes         VARCHAR(255) DEFAULT '------' NOT NULL,
    telefones           TEXT DEFAULT '------' NOT NULL,
    id_campus           INTEGER NOT NULL,
    id_cargo            INTEGER NOT NULL,
    id_setor            INTEGER NOT NULL,
    id_disciplina       INTEGER NOT NULL,
    id_setor_suap       INTEGER NOT NULL,
    id_jornada          INTEGER NOT NULL,
    id_categoria        INTEGER NOT NULL,
    id_funcao           INTEGER NOT NULL,
    
    CONSTRAINT pk_matricula_servidor PRIMARY KEY (matricula_servidor),
  
    CONSTRAINT fk_servidor_id_funcao FOREIGN KEY (id_funcao)
                REFERENCES funcao (id_funcao),
    CONSTRAINT fk_servidor_id_disciplina FOREIGN KEY (id_disciplina)
                REFERENCES disciplina_ingresso (id_disciplina),
    CONSTRAINT fk_servidor_id_categoria FOREIGN KEY (id_categoria)
                REFERENCES categoria (id_categoria),
    CONSTRAINT fk_servidor_id_cargo FOREIGN KEY (id_cargo)
                REFERENCES cargo (id_cargo),
    CONSTRAINT fk_servidor_id_setor FOREIGN KEY (id_setor)
                REFERENCES setor_siape (id_setor),
    CONSTRAINT fk_servidor_id_jornada FOREIGN KEY (id_jornada)
                REFERENCES jornada_trabalho (id_jornada),
    CONSTRAINT fk_servidor_id_campus FOREIGN KEY(id_campus)
                REFERENCES campus (id_campus),
    CONSTRAINT fk_servidor_id_setor_suap FOREIGN KEY (id_setor_suap)
                REFERENCES setor_suap(id_setor_suap)
);