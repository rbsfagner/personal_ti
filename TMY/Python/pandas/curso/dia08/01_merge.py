#%%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv",sep=";")
transacoes.head()

#%%

#Aqui eu precisei renomear a coluna pois ela estava diferente do banco ao fazer o merge
transacoes = transacoes.rename(columns={'IdCliente': 'idCliente'})

# %%
clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes.head()
# %%
# Aqui eu vejo como estão as colunas do indice que eu preciso
print("Colunas do DataFrame 1:", clientes.columns.tolist())
print("Colunas do DataFrame 2:", transacoes.columns.tolist())

# %%
#Merge igual ao do Sql
transacoes.merge(right=clientes, 
                 how='left', 
                 on=['idCliente'],
                 suffixes=["Transacao","Cliente"],
                 )
# %%
