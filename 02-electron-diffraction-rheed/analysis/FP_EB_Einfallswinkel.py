import numpy as np
import matplotlib.pyplot as plt

theta = np.array([1.5, 2.3, 3, 4.6, 5.7])
höhe = np.array([13.5, 13.75, 14, 14.2, 14.5])

coeffs=np.polyfit(theta, höhe, 1)

plt.scatter(theta, höhe, marker='x',label='Messwerte', color='deeppink')
plt.plot(theta, coeffs[0] * theta + coeffs[1],label='Fit', c='purple')
plt.xlabel(r"Einfallswinkel $\theta$ [°]")
plt.ylabel("Höhe [cm]")
plt.title("Variation der Einfallswinkel")
plt.grid(True, alpha=0.3)
plt.legend()

text = f"Fit: $y = {coeffs[0]:.3f}\\;\\theta \\, \\text{{cm/rad}} + {coeffs[1]:.3f}\\, \\text{{cm}}$"
plt.text(0.49, 0.15, text, transform=plt.gca().transAxes,
         fontsize=10,
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='pink'))

plt.savefig("FP_EB_Einfallswinkel.pdf", format="pdf")
plt.show()

