import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Daten laden
try:
    data = pd.read_csv('Bedampfung3DrahtMikroskop.csv', skiprows=1)
except:
    data = pd.read_csv('Bedampfung3DrahtMikroskop.csv', skiprows=1, sep=';')

# Spalten zuordnen
voltage = data.iloc[:, 0].values
red = data.iloc[:, 1].values
green = data.iloc[:, 2].values

# --- 1. FIT-FUNKTION DEFINIEREN ---
def sine_model(x, A, k, phi, C):
    return A * np.sin(k * x + phi) + C

# Startwerte schätzen
def get_p0(y):
    # Frequenz k ca. 7 (Periode ~0.9V)
    return [(np.max(y)-np.min(y))/2, 7.0, 0.0, np.mean(y)]

# Fit durchführen
popt_r, _ = curve_fit(sine_model, voltage, red, p0=get_p0(red))
popt_g, _ = curve_fit(sine_model, voltage, green, p0=get_p0(green))

# --- WICHTIG: Phasen normalisieren (-pi bis +pi) ---
# Das macht die Werte in der Legende lesbar und vergleichbar für die LaTeX-Rechnung
popt_r[2] = (popt_r[2] + np.pi) % (2 * np.pi) - np.pi
popt_g[2] = (popt_g[2] + np.pi) % (2 * np.pi) - np.pi

# --- 2. PLOTTING ---
fig, ax = plt.subplots(figsize=(8, 6))

# Glatte x-Achse für schöne Kurven
x_fit = np.linspace(voltage.min(), voltage.max(), 1000)

# Rot plotten
# Hinweis: Formel korrigiert zu sin(k*U + phi), da x-Achse die Spannung U ist
label_fit_r = (f'Fit Rot: $I(U)=A\\cdot \\sin(k\\cdot U+ \\phi)+C$ \n'
               f'$A={popt_r[0]:.1f}, k={popt_r[1]:.2f}, '
               f'\\phi={popt_r[2]:.2f}, C={popt_r[3]:.0f}$')

ax.plot(voltage, red, 'x', markersize=5, label='Messdaten Rot', c='darkred')
ax.plot(x_fit, sine_model(x_fit, *popt_r), 'r-', linewidth=1.5, label=label_fit_r)

# Grün plotten
label_fit_g = (f'Fit Grün: $I(U)=A\\cdot \\sin(k\\cdot U+ \\phi)+C$ \n'
               f'$A={popt_g[0]:.1f}, k={popt_g[1]:.2f}, '
               f'\\phi={popt_g[2]:.2f}, C={popt_g[3]:.0f}$')

ax.plot(voltage, green, 'x', markersize=5, label='Messdaten Grün', c='darkgreen')
ax.plot(x_fit, sine_model(x_fit, *popt_g), 'g-', linewidth=1.5, label=label_fit_g)

# Design
ax.set_title(r'Interferometer-Signale zur Phasenbestimmung mit Fit-Parametern')
ax.set_xlabel('Spannung U [V]')
ax.set_ylabel('Intensität I [a.u.]')
ax.grid(which='major', color='#CCCCCC', linewidth=0.8) 
ax.grid(which='minor', color='#EEEEEE', linestyle='--', linewidth=0.5)
ax.minorticks_on()

# Legende
ax.legend(loc='upper right', frameon=True, fancybox=False, edgecolor='black', facecolor='white', fontsize=10)

plt.tight_layout()
#plt.savefig('Interferometer_Fits.pdf')
plt.show()

# Nur zur Kontrolle in der Konsole ausgeben, damit du die Differenz direkt siehst
d_phi_raw = abs(popt_g[2] - popt_r[2])
d_phi_phys = min(d_phi_raw, 2*np.pi - d_phi_raw)
print(f"Phi Rot: {popt_r[2]:.4f}")
print(f"Phi Grün: {popt_g[2]:.4f}")
print(f"Physikalische Differenz für Rechnung: {d_phi_phys:.4f}")