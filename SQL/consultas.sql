-- Nesse documento iremos criar Views para ajudar nas consultas


-- Criando a Primeira View
CREATE VIEW servidorescampus AS
	SELECT  campus.campus as sigla,
			categoria.categoria as categoria,
	 COUNT	(servidor.matricula) AS nº_servidores
	  FROM	servidor
INNER JOIN	campus ON servidor.id_campus = campus.id_campus
INNER JOIN	categoria ON servidor.id_categoria = categoria.id_categoria
GROUP BY	campus.campus,
			categoria.categoria;
SELECT * FROM servidorescampus ORDER BY sigla;


-- Criando a Segunda View
CREATE VIEW docentesdisciplinas AS	
	SELECT	servidor.nome,
			disciplina_ingresso.disciplina AS disciplina
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN	categoria ON categoria.id_categoria = servidor.id_categoria
	 WHERE 	categoria.categoria = 'docente'
  ORDER BY	disciplina_ingresso.disciplina;
SELECT * FROM docentesdisciplinas;
