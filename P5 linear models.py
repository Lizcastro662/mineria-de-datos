import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

file_path = "C:/Users/lizca/Downloads/mineria de datos/base/roger-federer-data.csv"
df = pd.read_csv(file_path)

relevant_columns = ['player_ranking', 'tourney_singles_draw']
df_LIMP = df[relevant_columns]

df_LIMP = df_LIMP.dropna()  # Eliminar filas con valores faltantes
df_LIMP = df_LIMP.replace([float('inf'), -float('inf')], pd.NA).dropna()

x = df_LIMP['player_ranking']
y = df_LIMP['tourney_singles_draw']

x = sm.add_constant(x)  

model = sm.OLS(y,x).fit()  
print(model.summary())  

plt.scatter(df_LIMP['player_ranking'], df_LIMP['tourney_singles_draw'], alpha=0.5)
plt.xlabel('player ranking')
plt.ylabel('tourney singles draw')

plt.plot(df_LIMP['player_ranking'], model.predict(x), color='red')

img_path = "C:/Users/lizca/Downloads/mineria de datos/img/regresion.png"
plt.savefig(img_path)
plt.show()