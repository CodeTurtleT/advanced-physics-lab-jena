import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

pixel = np.array([51.5, 45, 41.5, 38, 36, 34.5, 33])
U_kV = np.array([10, 12.5, 15, 17.5, 20, 22.5, 25]) 

U_Volt = U_kV * 1000 

# Fit Funktion: a / sqrt(U) + b
def fit_func(u, a, b):
    return a * (1 / np.sqrt(u)) + b

#Fit
popt, pcov = curve_fit(fit_func, U_Volt, pixel) 

#Bereich für die Linie erstellen 
u_range = np.linspace(min(U_Volt), max(U_Volt), 100)
fit_curve = fit_func(u_range, *popt)

plt.figure(figsize=(8, 6))

#Plotten
plt.plot(U_Volt, pixel, 'x', color='rebeccapurple', label='Messdaten')
plt.plot(u_range, fit_curve, color='hotpink', label='Fit')

# Achsenbeschriftung anpassen
plt.xlabel("Beschleunigungsspannung U [V]")
plt.ylabel("Streakabstand l [Pixel]")
plt.title("Reziproke Abstände (Pixel) über Beschleunigungsspannung")
plt.grid(alpha=0.3)
plt.legend()

# Text-Block
text = f"Fit: $l(U) = \\left( \\frac{{{popt[0]:.1f}\\,\\sqrt{{\\mathrm{{V}}}}}}{{\\sqrt{{U}}}} {popt[1]:+.3f} \\right) \\mathrm{{px}}$"

plt.text(0.5, 0.65, text, transform=plt.gca().transAxes,
         fontsize=12,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='pink'))

plt.savefig("FP_EB_Spannung_Pixel.pdf", format="pdf")
plt.show()