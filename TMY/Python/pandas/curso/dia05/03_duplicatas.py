# %%

import pandas as pd

#%%

df = pd.DataFrame({
    "nome":['robson','taissa','yas','davi','janes','rf','bp'],
    "sobrenome":['fagner','fagner','vitorino','vieira','oliveira','silva', 'teste'],
    "salario":[10,20,30,50,50,60,100]
})

df
# %%
df.drop_duplicates

# %%
 
df = df.sort_values("salario", ascending=False)
df
# %%

# Parei no exercicio
