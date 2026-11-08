import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. DATEN LADEN ---
df = pd.read_csv('ESTrahl1.csv', delimiter=';')

x = df['x'].tolist()
# Liste der Spalten, die wir plotten wollen
y_cols = ['t1', 't6', 't10', 't15', 't20', 't25', 't30']
labels = ['1 min', '6 min', '10 min', '15 min', '20 min', '25 min', '30 min']

# --- 2. FARBEN DEFINIEREN (ROT OBEN) ---
# Wir nutzen die Colormap 'jet_r' (reversed), damit sie bei Rot startet und zu Blau geht.
# Alternativ ginge auch 'rainbow_r' oder 'gist_rainbow_r'.
num_lines = len(y_cols)
colors = plt.cm.jet_r(np.linspace(0, 1, num_lines))

# --- 3. PLOTTEN ---
plt.figure(figsize=(10, 6))

for i, col_name in enumerate(y_cols):
    plt.plot(x, df[col_name], 
             label=labels[i], 
             color=colors[i], 
             linewidth=2)

# Beschriftung
plt.xlabel('Abstand x [Pixel]', fontsize=12)
plt.ylabel('Intensität (Mean)', fontsize=12)
plt.title('Profilverlauf unter Elektronenbeschuss', fontsize=14)
plt.grid(True, alpha=0.3)

# Legende anzeigen
plt.legend(title="Bestrahlungsdauer", loc='upper right')

plt.tight_layout()
plt.savefig("FP_EB_Elektronenbeschuss1.pdf")
plt.show()