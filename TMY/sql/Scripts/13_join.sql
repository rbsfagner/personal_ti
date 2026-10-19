SELECT t1.*, -- Aqui pego tudo da tabela 1
		 t2.DescNomeProduto -- Aqui apenas essa coluna da tabela 2
		 	
FROM transacao_produto AS t1
   
LEFT JOIN produtos AS t2
ON t1.IdProduto = t2.IdProduto

--Stop on 7:59