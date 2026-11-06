#%%

import pandas as pd
clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes
# %%

#Removendo as linhas Nan, nesse caso, a linha inteira
clientes.dropna(how="all")
clientes.dropna(how="any")

# %%


df = pd.DataFrame({
    "nome": ["Robson", None, "Taissa", "Davi"],
    "idade": ["None", None, 43, 52],
    "salario": [3453, 4324, None , 5423],
})
#remove na de um data frame, apenas onde eu quero que seja.
df.dropna(how="all",subset=["idade","nome"])
# %%
df["idade"].fillna(0)


# %%
