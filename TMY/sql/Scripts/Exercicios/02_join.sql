--Em 2024, quantas transacoes de lovers tivemos?

select *
from transacoes as T1

LEFT JOIN transacao_produto as T2
ON t1.IdTransacao = t2.idProduto

where t1.DtCriacao >= '2024-01-01'
and t1.DtCriacao < '2025-01-01'


--parei no 24-38