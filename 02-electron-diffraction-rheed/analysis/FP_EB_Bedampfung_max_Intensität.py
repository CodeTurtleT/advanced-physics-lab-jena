import numpy as np
import matplotlib.pyplot as plt

maxI=np.array([120.324,114.622, 116.486, 118.297, 111.622, 109.595, 96.162, 106.486, 94.486, 91.622, 82.243, 83.324, 77.568, 68.162, 55.324, 33.000])
temp=np.array([37, 55, 80, 100, 130, 150, 180, 200,230,260, 280, 300, 325, 350, 375, 390])

plt.figure(figsize=(8, 5))

plt.plot(temp, maxI, 'D-', color='rebeccapurple', label='Messdaten der Bedampfung',markersize=6)

plt.xlabel(r"Temperatur $\vartheta$ [°C]")
plt.ylabel("Maximale Reflexintensität $I_{max}$")
plt.title("Intensitätsabnahme mit der Temperatur bei der Bedampfung")
plt.grid(True, alpha=0.5)
plt.legend()

plt.savefig("FP_EB_Bedampfung_max_Intensität.pdf", format="pdf")
plt.show()
