# %%
import pandas as pd

df = pd.read_csv(r"C:\Users\rbsfa\Documents\Git\personal_ti\TMY\Python\pandas\curso\data\transacoes.csv",sep=";")
df.head()

# %%
pontos = [ 10,1,1,1,50,100,130,30,25,50]
filtro = []

valores_50 = []
for i in pontos:
    filtro.append(i>=50)


resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i]) 
        
resultado   
# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)
filtro = brinquedo["idade"] >= 18
filtro
 
 # %%

filtro2 = df["QtdePontos"]>= 50
df[filtro2]
#%%
filtro3 = (df["QtdePontos"]>= 50) & (df["QtdePontos"] < 100) 
df[filtro3]
# %%
# Or, no caso ou
filtro4 = (df["QtdePontos"]==1) | (df["QtdePontos"]==100)
df[filtro4]
# %%
