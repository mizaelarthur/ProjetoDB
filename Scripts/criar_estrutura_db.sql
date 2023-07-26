CREATE DATABASE ProjetoDB;


CREATE TABLE "Servidor"(
    "matricula" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "telefones" VARCHAR(255) NULL,
    "curriculo_lattes" VARCHAR(255) NULL,
    "url_foto_75x100" VARCHAR(255) NULL,
    "categoria" BIGINT NOT NULL,
    "cargo" BIGINT NOT NULL,
    "setor_siape" BIGINT NOT NULL,
    "disciplina_ingresso" BIGINT NOT NULL,
    "setor_suap" BIGINT NOT NULL,
    "funcao" BIGINT NOT NULL,
    "jornada_trabalho" BIGINT NOT NULL,
    "campus" BIGINT NOT NULL
);
ALTER TABLE
    "Servidor" ADD PRIMARY KEY("matricula");
CREATE TABLE "Jornada_Trabalho"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Jornada_Trabalho" ADD PRIMARY KEY("id");
ALTER TABLE
    "Jornada_Trabalho" ADD CONSTRAINT "jornada_trabalho_nome_unique" UNIQUE("nome");
CREATE TABLE "Cargo"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Cargo" ADD PRIMARY KEY("id");
ALTER TABLE
    "Cargo" ADD CONSTRAINT "cargo_nome_unique" UNIQUE("nome");
CREATE TABLE "Setor_siape"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Setor_siape" ADD PRIMARY KEY("id");
ALTER TABLE
    "Setor_siape" ADD CONSTRAINT "setor_siape_nome_unique" UNIQUE("nome");
CREATE TABLE "Categoria"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Categoria" ADD PRIMARY KEY("id");
ALTER TABLE
    "Categoria" ADD CONSTRAINT "categoria_nome_unique" UNIQUE("nome");
CREATE TABLE "Funcao"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Funcao" ADD PRIMARY KEY("id");
ALTER TABLE
    "Funcao" ADD CONSTRAINT "funcao_nome_unique" UNIQUE("nome");
CREATE TABLE "Disciplina_ingresso"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Disciplina_ingresso" ADD PRIMARY KEY("id");
ALTER TABLE
    "Disciplina_ingresso" ADD CONSTRAINT "disciplina_ingresso_nome_unique" UNIQUE("nome");
CREATE TABLE "Campus"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Campus" ADD PRIMARY KEY("id");
ALTER TABLE
    "Campus" ADD CONSTRAINT "campus_nome_unique" UNIQUE("nome");
CREATE TABLE "Setor_suap"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Setor_suap" ADD PRIMARY KEY("id");
ALTER TABLE
    "Setor_suap" ADD CONSTRAINT "setor_suap_nome_unique" UNIQUE("nome");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_jornada_trabalho_foreign" FOREIGN KEY("jornada_trabalho") REFERENCES "Jornada_Trabalho"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_setor_siape_foreign" FOREIGN KEY("setor_siape") REFERENCES "Setor_siape"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_campus_foreign" FOREIGN KEY("campus") REFERENCES "Campus"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_cargo_foreign" FOREIGN KEY("cargo") REFERENCES "Cargo"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_disciplina_ingresso_foreign" FOREIGN KEY("disciplina_ingresso") REFERENCES "Disciplina_ingresso"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_setor_suap_foreign" FOREIGN KEY("setor_suap") REFERENCES "Setor_suap"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_funcao_foreign" FOREIGN KEY("funcao") REFERENCES "Funcao"("id");
ALTER TABLE
    "Servidor" ADD CONSTRAINT "servidor_categoria_foreign" FOREIGN KEY("categoria") REFERENCES "Categoria"("id");