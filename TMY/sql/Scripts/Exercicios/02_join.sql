SELECT COUNT(DISTINCT t1.Idtransacao)

from transacoes as T1

LEFT JOIN transacao_produto as T2
ON t1.IdTransacao = t2.IdTransacao

left join produtos as t3
on t2.IdProduto = t3.IdProduto

where t1.DtCriacao >= '2024-01-01'
and t1.DtCriacao < '2025-01-01'
and t3.DescCategoriaProduto = 'lovers'