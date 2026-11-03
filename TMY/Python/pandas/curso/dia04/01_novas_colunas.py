# %%
import pandas as pd
import numpy as np

df = pd.read_csv("data/clientes.csv",sep=";")
df.head()
# %%

#aqui eu somo 100 pontos ao quantidade de pontos
df["pontos + 100"] = df["qtdePontos"] + 100

# %%
# Forma manual
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i+100)
nova_coluna
# %%
df
# %%

# somei as duas colunas e criei uma nova
df["email_twitch"] = df["flEmail"] + df["flTwitch"]

# %%
df["qtdePontos"].describe()

# %%
#chamando nunmpy para apliar log 
np.log(df["qtdePontos"] + 1)
# %%

# Parei na parte de ordenação