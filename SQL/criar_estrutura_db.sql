-- CREATE DATABASE ProjetoDB; # Caso queira,  retire o comentario e coloque o nome do seu BD


CREATE TABLE "servidor"(
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
    "servidor" ADD PRIMARY KEY("matricula");
CREATE TABLE "jornada_trabalho"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "jornada_trabalho" ADD PRIMARY KEY("id");
ALTER TABLE
    "jornada_trabalho" ADD CONSTRAINT "jornada_trabalho_nome_unique" UNIQUE("nome");
CREATE TABLE "cargo"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "cargo" ADD PRIMARY KEY("id");
ALTER TABLE
    "cargo" ADD CONSTRAINT "cargo_nome_unique" UNIQUE("nome");
CREATE TABLE "setor_siape"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "setor_siape" ADD PRIMARY KEY("id");
ALTER TABLE
    "setor_siape" ADD CONSTRAINT "setor_siape_nome_unique" UNIQUE("nome");
CREATE TABLE "categoria"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "categoria" ADD PRIMARY KEY("id");
ALTER TABLE
    "categoria" ADD CONSTRAINT "categoria_nome_unique" UNIQUE("nome");
CREATE TABLE "funcao"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "funcao" ADD PRIMARY KEY("id");
ALTER TABLE
    "funcao" ADD CONSTRAINT "funcao_nome_unique" UNIQUE("nome");
CREATE TABLE "disciplina_ingresso"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "disciplina_ingresso" ADD PRIMARY KEY("id");
ALTER TABLE
    "disciplina_ingresso" ADD CONSTRAINT "disciplina_ingresso_nome_unique" UNIQUE("nome");
CREATE TABLE "campus"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "campus" ADD PRIMARY KEY("id");
ALTER TABLE
    "campus" ADD CONSTRAINT "campus_nome_unique" UNIQUE("nome");
CREATE TABLE "setor_suap"(
    "id" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "setor_suap" ADD PRIMARY KEY("id");
ALTER TABLE
    "setor_suap" ADD CONSTRAINT "setor_suap_nome_unique" UNIQUE("nome");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_jornada_trabalho_foreign" FOREIGN KEY("jornada_trabalho") REFERENCES "jornada_trabalho"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_setor_siape_foreign" FOREIGN KEY("setor_siape") REFERENCES "setor_siape"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_campus_foreign" FOREIGN KEY("campus") REFERENCES "campus"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_cargo_foreign" FOREIGN KEY("cargo") REFERENCES "cargo"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_disciplina_ingresso_foreign" FOREIGN KEY("disciplina_ingresso") REFERENCES "disciplina_ingresso"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_setor_suap_foreign" FOREIGN KEY("setor_suap") REFERENCES "setor_suap"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_funcao_foreign" FOREIGN KEY("funcao") REFERENCES "funcao"("id");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_categoria_foreign" FOREIGN KEY("categoria") REFERENCES "categoria"("id");