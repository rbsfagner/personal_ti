SELECT * from transacao_produto

LEFT JOIN produtos

on transacao_produto.IdProduto = produtos.Idproduto

limit 10