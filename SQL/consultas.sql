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


