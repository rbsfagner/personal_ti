#%%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")
# %%
df
# %%
#CONVERTENDO PARA FLOT OU O TIPO DE DADO QUE EU PRECISAR
df["qtdePontos"].astype(float)


# %%
#troquei pelo valor que eu precisava
df["DtCriacao"].replace({
    "2025-11-13 12:03:56.114":"2030-11-13 12:03:56.114"
    })

# %%
