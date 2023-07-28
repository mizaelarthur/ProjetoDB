CREATE VIEW consultas_servidores_campus AS
	SELECT  campus.ncampus as sigla,
			categoria.ncategoria as categoria,
	 COUNT	(servidor.matricula_servidor) AS qt_servidores
	  FROM	servidor
INNER JOIN	campus ON servidor.id_campus = campus.id_campus
INNER JOIN	categoria ON servidor.id_categoria = categoria.id_categoria
GROUP BY	campus.ncampus,
			categoria.ncategoria;
SELECT * FROM consultas_servidores_campus ORDER BY sigla;





CREATE VIEW consultas_docentes_disciplinas AS	
	SELECT	servidor.nome,
			disciplina_ingresso.ndisciplina AS disciplina
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN	categoria ON categoria.id_categoria = servidor.id_categoria
	 WHERE 	categoria.ncategoria = 'docente'
  ORDER BY	disciplina_ingresso.ndisciplina;
SELECT * FROM consultas_docentes_disciplinas;





CREATE VIEW consultas_disciplinas_campus AS	
	SELECT	disciplina_ingresso.ndisciplina AS disciplina,
			campus.ncampus as sigla,
	 COUNT	(servidor.matricula_servidor) AS qt_disciplinas
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN	categoria ON categoria.id_categoria = servidor.id_categoria
INNER JOIN	campus ON servidor.id_campus = campus.id_campus
	 WHERE 	categoria.ncategoria = 'docente'
  GROUP BY	disciplina_ingresso.ndisciplina,
  			campus.ncampus;
SELECT * FROM consultas_disciplinas_campus ORDER BY sigla;