import numpy as np
import matplotlib.pyplot as plt

time=np.array([0, 1, 2.5, 5, 7.5, 10, 12.5, 15, 23])
mean_substrat=np.array([57.615, 78.341, 87.367, 95.330, 97.946, 105.436 ,108.140, 104.348, 113.414])
mean_adsorbat=np.array([40.648,58.291, 69.960, 84.351, 94.754, 108.775, 117.961, 118.797, 168.476])

plt.figure(figsize=(8, 5))

plt.plot(time, mean_substrat, '-*', label='Substrat (Ag)', color='hotpink')
plt.plot(time, mean_adsorbat, '-D', label='Adsorbat (KCl)', color='rebeccapurple',markersize=6)

plt.xlabel('Zeit [min]')
plt.ylabel('Intensität (Mean)')
plt.title('erste KCL Bedampfung: Intensitätsverlauf')
plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig("FP_EB_erste_Bedampfung.pdf", format="pdf")
plt.show()