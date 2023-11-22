import pandas as pd
import matplotlib.pyplot as plt
import os 

file_path = "C:/Users/lizca/Downloads/mineria de datos/base/datoslimpios.csv"
df = pd.read_csv (file_path)

directory = "C:/Users/lizca/Downloads/mineria de datos/img"

if not os.path.exists(directory):
    os.makedirs(directory)

df_15 = df.head(15)
fig,ax=plt.subplots()

x= df_15['tourney_year']
y= df_15 ['tourney_name']
ax.bar (x,y)

ax.set_xlabel("year")
ax.set_ylabel("name")
ax.set_title("Ranking de Roger Federer")

plt.xticks(rotation=90)
img_path_1 = os.path.join(directory, 'Rangos')
plt.savefig(img_path_1)
plt.show

fig, ax=plt.subplots()

x = df_15['tourney_conditions']
y = df_15['tourney_surface']
ax.bar(x, y)

ax.set_xlabel("conditions")
ax.set_ylabel("surface")
ax.set_title("Condiciones de juego")

plt.xticks(rotation=90)

img_path_2 = os.path.join(directory, 'ccondicionesdejuego.png')
plt.savefig(img_path_2)
plt.show()