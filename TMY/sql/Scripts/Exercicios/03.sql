-- Qual mes tivemos mais lista de presença assinada?

SELECT * FROM transacoes AS t1

LEFT JOIN transacao_produto AS t2
ON	t1.idTransacao = t2.IdTransacao

LEFT JOIN produtos AS t3

ON t2.IdProduto = t3.IdProduto

WHERE	DescProduto = ' Lista de presença'

LIMIT 100