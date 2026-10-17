#%%

import pandas as pd

df = pd.read_csv(r"C:\Users\rbsfa\Documents\Git\personal_ti\TMY\Python\pandas\curso\data\transacao_produto.csv",sep=";")
df.head()


# %%

filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 11)
filtro

# %%

df["IdProduto"].isin([5,11])
# %%
