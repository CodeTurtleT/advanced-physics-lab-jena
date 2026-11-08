import numpy as np
import matplotlib.pyplot as plt

# --- DATEN ---
temp = np.array([30, 61, 100, 140, 163, 200, 230, 260, 280, 310, 330, 350, 370, 385, 400])

min=np.array([14, 11, 20, 20, 21, 20, 19, 17, 21, 18, 15, 19, 18, 15, 16])

max=np.array([157, 154, 149, 144, 140, 133, 129, 113, 107, 90, 82, 79, 68, 69, 58])

mean=np.array([45.662, 42.075, 42.388, 41.793, 42.116, 40.807, 40.268, 37.033, 40.820, 38.203, 36.973, 35.288, 34.753, 33.806, 31.670])

# --- PLOTTEN ---
plt.figure(figsize=(8, 6))

# Bereich zwischen Min und Max schattieren (zeigt die "Signalamplitude")
plt.fill_between(temp, min, max, color='pink', alpha=0.1, label='Signalbereich')

plt.plot(temp, max, color='hotpink', label='Max (Peak)')
plt.plot(temp, mean, color='rebeccapurple', label='Mean (Durchschnitt)')
plt.plot(temp, min, color='steelblue', label='Min (Hintergrund)')

plt.xlabel(r'Temperatur $\vartheta$ [°C]') 
plt.ylabel('Intensität')
plt.title('Temperaturabhängigkeit der Reflex- und Hintergrundintensität während des Ausheilens')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("FP_EB_Ausheilen_MinMax.pdf")
plt.show()

