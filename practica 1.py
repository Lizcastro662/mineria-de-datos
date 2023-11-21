import pandas as pd

file_path = "C:/Users/lizca/Downloads/base/roger-federer-data.csv"
df = pd.read_csv (file_path)

df_clean = df [['player_ranking','tourney_year', 'tourney_name','tourney_location'
,'tourney_dates', 'tourney_conditions', 'tourney_surface'
, 'opponent_name', 'match_win_loss','match_score']]

ruta_guardado = "C:/Users/lizca/Downloads/base/datoslimpios.csv"
df_clean.to_csv (ruta_guardado, index= False)

print(df_clean)
