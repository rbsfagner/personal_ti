#%%

import pandas as pd

# %%
df = pd.read_parquet("dados/dados_clones.parquet")
df
# %%
from sklearn import tree
arvore = tree.DecisionTreeClassifier(random_state=42)

# %%

df['General Jedi encarregado'].unique()

#%%

y = df[Status]
# %%
df
# %%
