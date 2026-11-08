import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

m = 9.10938356e-31       # kg
e = 1.60217663e-19       # C
hbar = 1.0545718e-34     # Js
a = 4.0853e-10           # m
G = 1.57e10              # 1/m  (Schreibweise korrigiert)
L = 0.2                  # m

U_V  = 1000 * np.linspace(10, 25.5, 100)  # Volt, 10–30 kV
U_Ve = 1000 * np.array([10, 12.5, 15, 17.5, 20, 22.5, 25])  # Volt

# Theorie: Wellenzahl
def theorie_k0(U):
    return np.sqrt(2 * m * e * U) / hbar

# Theorie: Abstand l(U)
def theorie_l(k0):
            return G * L / k0

k0_values = theorie_k0(U_V)
l_theo = theorie_l(k0_values)

# Daten
U_Ve_kV = np.array([10, 12.5, 15, 17.5, 20, 22.5, 25])  # kV
l_kali = np.array([6.09, 5.32, 4.91, 4.50, 4.26, 4.08, 3.90])  # mm

# Theorie: l(U)
def lU(U):
    return 4.91 * np.sqrt(15 / U)

lU_values = lU(U_Ve_kV)

# Fitfunktion: l(U) = A / sqrt(U) + C
def inv_sqrt_fit(U, A, C):
    return A / np.sqrt(U) + C

# Fit auf kalibrierte Messwerte
params_kali, cov_kali = curve_fit(inv_sqrt_fit, U_Ve_kV, l_kali, p0=[10, 0])
A_k, C_k = params_kali

# Fit auf l(U)
params_lU, cov_lU = curve_fit(inv_sqrt_fit, U_Ve_kV, lU_values, p0=[10, 0])
A_u, C_u = params_lU

# Fitkurven erzeugen
U_plot = np.linspace(10, 25, 300)
fit_kali_curve = inv_sqrt_fit(U_plot, A_k, C_k)
fit_lU_curve = inv_sqrt_fit(U_plot, A_u, C_u)

# Plot
plt.figure(figsize=(10, 7))

plt.plot(U_Ve_kV, l_kali, '*', label='Kalibrierte Messwerte', c='steelblue')
plt.plot(U_plot, fit_kali_curve, '-', label=r"Fit $l_{kali}(U)$", c='steelblue')

plt.plot(U_Ve_kV, lU_values, 'x', label='l(U) aus Gl. (4.1)', c='rebeccapurple')
plt.plot(U_plot, fit_lU_curve, '--', label='Fit l(U)', c='rebeccapurple')

plt.plot(U_V / 1000, 1000 * l_theo, label='Theoriewerte', c='hotpink')  # mm

plt.xlabel("Beschleunigungsspannung U [kV]")
plt.ylabel("Streakabstand l [mm]")
plt.title(r"Streakabstand $l$ vs. Beschleunigungsspannung $U$: Theorie vs. Experiment",fontsize=16)
plt.grid(True, alpha=0.3)
plt.legend(facecolor='white', fontsize=12)

# Fitparametertext für Messwerte
text1 = (
    r"Fit $l_{\mathrm{kali}}(U)$:" + "\n"
    rf"$ = {A_k:.3f}/\sqrt{{U}} + {C_k:.3f}\,\mathrm{{mm}}$"
)

# Fitparametertext für l(U)
text2 = (
    r"Fit $l(U)$:" + "\n"
    rf"$l(U) = {A_u:.3f}/\sqrt{{U}} + {C_u:.3f}\,\mathrm{{mm}}$"
)

plt.text(
    0.55, 0.70, text1, transform=plt.gca().transAxes,
    fontsize=13,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='steelblue')
)

plt.text(
    0.55, 0.55, text2, transform=plt.gca().transAxes,
    fontsize=13,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='rebeccapurple')
)

plt.tight_layout()
#plt.savefig("FP_EB_Spannung_Vergleich_Final.pdf")
plt.show()

