#%%
import pandas as pd
import matplotlib.pyplot as plt
# %%
df = pd.read_parquet("dados/dados_clones.parquet")
df
# %%
from sklearn import tree
arvore = tree.DecisionTreeClassifier(random_state=42,max_leaf_nodes=4)

# %%
features = ["Massa(em kilos)","Estatura(cm)"]
target = 'Status '

#%%
X = df[features]
y = df[target]

# %%
arvore.fit(X,y)

# %%
print(df.columns.tolist())

#%%

plt.figure(dpi=400)

tree.plot_tree(arvore,
               feature_names=features,
               class_names=arvore.classes_,
               filled=True)

# %%
