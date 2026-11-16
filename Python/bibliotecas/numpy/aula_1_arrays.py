# %%
import numpy as np
# %%
# Aqui vou importar essa matriz = 
#    1 2 3
#    4 5 6 
# %%
np.__version__
# %%
X = np.array( [[1,2,3],[4,5,6]] ,dtype=np.int32)
#%%

type(X)

# %%
X
# %%
# Mostradando o tamanho da matriz
X.shape
# %%
#Guardando dimensões dentro de variáveio

n,m = X.shape

# %%
n #Valor de n ( linhas )
# %%
m # Valor de m ( Colunas )
# %%
n = X.shape[0]
# %%
m = X.shape[1]
# %%
