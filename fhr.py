# %% [markdown]
# # Graficare FHR vs VCASB

# %%
import os
import numpy as np

import json
import matplotlib.pyplot as plt

# %% [markdown]
# ###### Funzione estrapola vcasb

# %%

def vcasb(cartella):

    files_json = [f for f in os.listdir(cartella) if f.endswith('.json')]  
    
    vcasbout=[]

    for file in files_json:
        percorso_file_json = os.path.join(cartella, file)
        with open(percorso_file_json, 'r', encoding='utf-8') as f:
            json_data = f.read()
        dictio = json.loads(json_data)
        vcasb_i=dictio["vcasb"]
        vcasbout.append(vcasb_i)
    return vcasbout 

# %%
def npy(cartella):

    files_npz = [f for f in os.listdir(cartella) if f.endswith('.npz')]
    noiseoccout=[]
    for file in files_npz:
        percorso_file_npz = os.path.join(cartella, file)
        data=np.load(percorso_file_npz)
        noiseocc=data['noiseocc'].astype(float)
        noiseoccout.append(noiseocc)
        
    return noiseoccout
        

# %% [markdown]
# #### Esecuzione programmi

# %%
cartella = r"C:\Users\giono\Desktop\UNIVERSITA\programmazione\python\dati\fhr"

# %%
vcasbout=vcasb(cartella)
noiseoccout=npy(cartella)
sorted(vcasbout)

# %%
sorted(noiseoccout)

# %%
output = os.path.join(cartella, 'plot.txt')
f_out = open(output,"w")

# %%
#plt.yscale('log')
plt.scatter(vcasbout,noiseoccout)


# %%



