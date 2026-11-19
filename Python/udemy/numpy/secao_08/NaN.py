## 25 : Lidando com ausencia de números

# %%
import numpy as np

# %%
x = np.array([1, 2.0, np.nan, 3, np.nan, 5])
x4 = np.array([1, 2, np.nan, 5, np.nan, 2, 1, 5, 8, 9, np.nan, 11, 3, 2, 7, np.nan])

## 26 : Como remover NaNs de Arrays

# %%
lista = []
for i in x4:
    if np.isnan(i):
        print("-->NAN")
    else:
        lista.append(i)
        print(i)
# %%
x5 = np.array(lista)
# %%

# Aqui estou negando tudo que for NAN
x6 = x4[~np.isnan(x4)]
# %%
x6
# %%
