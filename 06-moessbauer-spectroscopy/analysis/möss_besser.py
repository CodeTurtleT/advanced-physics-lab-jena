import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import pandas as pd

# ==========================================
# 1. ROBUSTES PARSING (XML)
# ==========================================
tree = ET.parse("20260512.30_minuten_mcs.ws5")
root = tree.getroot()
data_text = root.find('data').text.strip().split('\n')
y_raw = np.array([float(val) for val in data_text])

# ==========================================
# 2. SPEKTRUM FALZEN & NORMALIREN (Triangle Drive)
# ==========================================
y_norm = y_raw / np.max(y_raw)
half_len = len(y_norm) // 2

y_left = y_norm[:half_len]
y_right = y_norm[half_len:-1]
y_short = (y_left + y_right[::-1]) / 2  # Faltung (Mittelung)

# ==========================================
# 3. AUTOMATISCHE PEAK-SUCHE (Signal Processing)
# ==========================================
# Da wir Absorptionspeaks (Minima) suchen, invertieren wir das Signal temporär
peaks, properties = find_peaks(-y_short, prominence=0.01, distance=30)
peak_channels = peaks[:6]  # Wir erwarten 6 Peaks beim Eisen-Sextett

print(f"Automatisch gefundene Peaks bei Kanälen: {peak_channels}")

# ==========================================
# 4. KALIBRIERUNG DER X-ACHSE (Velocity)
# ==========================================
v_factor = 0.02793
channel_offset = 258 - (1/3) # Kalibrierungs-Offset
velocity = v_factor * (np.arange(len(y_short)) - channel_offset)

# ==========================================
# 5. LORENTZ-FIT
# ==========================================
def lorentz(v, A, v0, gamma):
    return (A / np.pi) * (gamma / ((v - v0)**2 + gamma**2))

def mose_sextet(v, y0, *params):
    y = y0
    for i in range(0, 18, 3):
        y += lorentz(v, params[i], params[i+1], params[i+2])
    return y

# Dynamische Startparameter aus der automatischen Peak-Suche
y0_guess = np.max(y_short)
initial_guesses = [y0_guess]
for p_idx in peak_channels:
    initial_guesses.extend([-0.05, velocity[p_idx], 0.15]) # Amplitude, Center, Gamma

popt, pcov = curve_fit(mose_sextet, velocity, y_short, p0=initial_guesses)

# ==========================================
# 6. PROFESSIONELLER PLOT
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(velocity, y_short, '.', color='darkgrey', label='Messdaten', alpha=0.7)
ax.plot(velocity, mose_sextet(velocity, *popt), color='crimson', linewidth=2, label='6-Lorentz Fit')

ax.set_xlabel('Geschwindigkeit (mm/s)', fontsize=12)
ax.set_ylabel('Normierte Zählrate', fontsize=12)
ax.set_title(r'Mößbauer-Spektrum von $\alpha$-Fe', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(frameon=True, fontsize=11)
plt.tight_layout()
plt.show()

# ==========================================
# 7. EXPORT
# ==========================================
df_export = pd.DataFrame({'velocity_mm_s': velocity, 'normalized_counts': y_short})
df_export.to_csv('moessbauer_fe_clean_data.csv', index=False)