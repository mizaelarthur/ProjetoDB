CREATE TABLE cargo(
    id_cargo    SERIAL,
    cargo  VARCHAR(255),
    CONSTRAINT pk_id_cargo PRIMARY KEY (id_cargo),
    CONSTRAINT un_cargo UNIQUE(cargo)
);