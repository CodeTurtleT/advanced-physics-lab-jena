import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re 

# --- 1. DATEN LADEN ---
# Wir nutzen den relativen Pfad, damit es überall funktioniert
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'ausheilen.csv')

try:
    # WICHTIG: Standard-CSV (Komma als Trenner, Punkt als Dezimal)
    df = pd.read_csv(csv_path)
    print("Daten erfolgreich geladen!")
    print("Spalten in der Datei:", df.columns.tolist())
except FileNotFoundError:
    print(f"Fehler: Datei nicht gefunden unter {csv_path}")
    exit()

# Spaltennamen bereinigen (Leerzeichen entfernen)
df.columns = df.columns.str.strip()

# --- 2. DATEN ZUORDNEN ---
# X-Achse
if 'x' in df.columns:
    x_data = df['x']
else:
    print("Warnung: Spalte 'x' nicht gefunden, nehme die erste Spalte als Index.")
    x_data = df.iloc[:, 0]

# Y-Achsen (Alle Spalten außer ' ' und 'x')
# Wir suchen alle Spalten, die '(....jpg)' im Namen haben oder einfach ab Spalte 3
y_cols = [col for col in df.columns if 'jpg' in col]

# Falls das Pattern nicht passt, nehmen wir einfach alle ab der 3. Spalte (Index 2)
if not y_cols:
    y_cols = df.columns[2:]

# --- 3. FARBEN & LABELS ---
num_lines = len(y_cols)
colors = plt.cm.jet_r(np.linspace(0, 1, num_lines))

# --- 4. PLOTTEN ---
plt.figure(figsize=(10, 6))

for i, col_name in enumerate(y_cols):
    # Label extrahieren: Aus "1 (30.jpg)" machen wir "30"
    # Wir suchen nach Zahlen zwischen '(' und '.'
    match = re.search(r'\((\d+)', col_name)
    if match:
        time_label = match.group(1) # Das ist die Zahl (z.B. 30)
    else:
        time_label = col_name # Fallback, falls Format anders ist

    plt.plot(x_data, df[col_name], 
             label=f"{time_label} °C", 
             color=colors[i], 
             linewidth=2)

# Beschriftung
plt.xlabel('Position [Pixel]]', fontsize=12)
plt.ylabel('Intensität (Mean)', fontsize=12)
plt.title('Profilverlauf beim Ausheilen', fontsize=14)
plt.grid(True, alpha=0.3)

# Legende
plt.legend(title="Temperatur", loc='upper left', bbox_to_anchor=(0.2, 1))

plt.tight_layout()
#plt.savefig("FP_EB_Ausheilen_Position.pdf")
plt.show()