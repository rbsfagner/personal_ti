-- Qual é a categoria de produtos mais vendidos

SELECT t2.DescCategoriaProduto,
       count(distinct t1.IdTransacao)


FROM transacao_produto AS T1

LEFT JOIN produtos AS t2

ON t1.idProduto = t2.idProduto


group by t2.DescCategoriaProduto
order by count(distinct t1.IdTransacao) desc