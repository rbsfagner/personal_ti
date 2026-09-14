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

brinquedo["idade"] >= 18

# %%

parei no 12:50