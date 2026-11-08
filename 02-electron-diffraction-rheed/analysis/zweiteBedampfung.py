import numpy as np
import matplotlib.pyplot as plt

time=np.array([0, 2.5, 5, 7.5, 10, 13.33, 19, 26, 30])

#mean_substrat=np.array([144.020, 148.279, 140.797, 146.754, 149.999, 149.238, 153.667, 149.465, 157.390])
mean_adsorbat=np.array([118.603, 126.447, 124.084, 132.178, 138.480, 140.722, 149.800, 149.906, 159.882])

plt.figure(figsize=(8, 5))

#plt.plot(time, mean_substrat, '-*', label='Substrat (Ag)', color='hotpink')
plt.plot(time, mean_adsorbat, '-D', label='Adsorbat (KCl)', color='rebeccapurple', markersize=6)

plt.xlabel('Zeit [min]')
plt.ylabel('Intensität (Mean) KCL')
plt.title('2. Bedampfungsphase: Intensitätszunahme KCl')
plt.grid(True, alpha=0.3)
plt.legend()

plt.savefig("FP_EB_zweite_Bedampfung.pdf", format="pdf")
plt.show()
#frage hier eher wie vile sinn es noch macht da substrat werte noch mehr verfälsht sind
