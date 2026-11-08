import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Daten
U_kV = np.array([10, 12.5, 15, 17.5, 20, 22.5, 25]) 
l = np.array([19.086, 16.677, 15.380, 14.083, 13.342, 12.786, 12.230]) # Einheit: 1/nm
U_Volt = U_kV * 1000 

# Fit Funktion
def fit_func(u, a, b):
    return a * (1 / np.sqrt(u)) + b

# Fit durchführen
popt, pcov = curve_fit(fit_func, U_Volt, l) 

# Werte für die glatte Linie
u_range = np.linspace(min(U_Volt), max(U_Volt), 100)
fit_curve = fit_func(u_range, *popt)

plt.figure(figsize=(8, 6))

# Plotten
plt.plot(U_Volt, l, 'x', color='deeppink', label='Messdaten')
plt.plot(u_range, fit_curve, color='rebeccapurple', label='Fit')

# Achsen
plt.xlabel("Beschleunigungsspannung U [V]")
plt.ylabel("Streakabstand l [$\\mathrm{nm}^{-1}$]") 
plt.title("Reziproke Abstände über Beschleunigungsspannung")
plt.grid(alpha=0.3)
plt.legend()

# --- KORREKTUR ---
# Die Einheit am Ende bezieht sich auf das Ergebnis l.
# :+.3f sorgt dafür, dass das Vorzeichen von b automatisch stimmt.
text = f"Fit: $l(U) = \\left( \\frac{{{popt[0]:.1f}\\,\\sqrt{{\\mathrm{{V}}}}}}{{\\sqrt{{U}}}} {popt[1]:+.3f} \\right) \\mathrm{{nm}}^{{-1}}$"

plt.text(0.5, 0.65, text, transform=plt.gca().transAxes,
         fontsize=12,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='pink'))

plt.savefig("FP_EB_Spannung_1_nm.pdf", format="pdf")
plt.show()