-- Nesse documento iremos criar Views para ajudar nas consultas


-- Criando a Primeira View
CREATE VIEW servidores_campus AS
	SELECT  campus.nome as sigla,
			categoria.nome as categoria,
	 COUNT	(servidor.matricula) AS qt_servidores
	  FROM	servidor
INNER JOIN	campus ON servidor.campus = campus.id
INNER JOIN	categoria ON servidor.categoria = categoria.id
GROUP BY	campus.nome,
			categoria.nome;
--FAZ A CONSULTA A PARTIR DA VIEW			
SELECT * FROM servidores_campus ORDER BY sigla;

--	Criando a Segunda View
CREATE VIEW docentes_disciplinas AS	
	SELECT	servidor.nome,
			disciplina_ingresso.nome AS disciplina
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.disciplina_ingresso = disciplina_ingresso.id
INNER JOIN	categoria ON categoria.id = servidor.categoria
	 WHERE 	categoria.nome = 'docente' -- Adicionando condição de Docente para filtragem
  ORDER BY	disciplina_ingresso.nome;

--FAZ A CONSULTA A PARTIR DA VIEW
SELECT * FROM docentes_disciplinas;

-- Criando Terceira View
CREATE VIEW disciplinas_campus AS	
	SELECT	disciplina_ingresso.nome AS disciplina,
			campus.nome as sigla,
	 COUNT	(servidor.matricula) AS qt_disciplinas
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.disciplina_ingresso = disciplina_ingresso.id
INNER JOIN	categoria ON categoria.id = servidor.categoria
INNER JOIN	campus ON servidor.campus = campus.id
	 WHERE 	categoria.nome = 'docente' -- Adicionando condição de Docente para filtragem
  GROUP BY	disciplina_ingresso.nome,
  			campus.nome;

--FAZ A CONSULTA A PARTIR DA VIEW
SELECT * FROM disciplinas_campus ORDER BY sigla;