#%%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv",sep=";")
# %%
df.shape #Quantidade de linhas
#%%
df.info(memory_usage="deep")
#%%
df.dtypes
#%%
renamed_columns = {
                        "QtdePontos":"qtPontos",
                        "DescSistemaOrigem":"SistemaOrigem"
}
df.rename(columns=renamed_columns, inplace=True)
# %%
colunas =["IdCliente","qtPontos"]
colunas
# %%
df[colunas]
# %%
# SELECT * FROM DF 
df
# %%
# SELECT idCliente FROM df
df[['IdCliente']]

# %%
# SELECT idCliente, qtPontos FROM df LIMIT 5

df[['IdCliente','qtPontos']].head()