#%%
import pandas as pd
clientes = pd.read_csv("../data/clientes.csv", sep=";")
# %%
clientes 
# %%
#Maior quantidade de pontos em ordem
clientes["qtdePontos"].sort_values()


 

# %%
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
                  .head(5)["idCliente"])

# %%
type(top_5)
# %%

