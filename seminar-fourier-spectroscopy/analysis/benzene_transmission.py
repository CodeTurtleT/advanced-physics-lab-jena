"""Near-infrared transmission spectrum of benzene (d = 20 mm), measured with the FTIR spectrometer.

Transmission = spectrum of the tungsten lamp through the benzene cell / spectrum of the lamp alone.
Both spectra are averaged in 20 cm^-1 bins to reduce noise.
"""
import numpy as np
import matplotlib.pyplot as plt


def load(filename):
    data = np.loadtxt(filename, converters=lambda s: float(s.replace(",", ".")), encoding="latin-1")
    return 1e7 / data[:, 0], data[:, 1]  # wavelength (nm) -> wavenumber (cm^-1)


def bin_spectrum(wavenumber, intensity, edges):
    idx = np.digitize(wavenumber, edges)
    return np.array([intensity[idx == i].mean() if np.any(idx == i) else np.nan
                     for i in range(1, len(edges))])


edges = np.arange(3800, 10600, 20.0)
centres = (edges[:-1] + edges[1:]) / 2

lamp = bin_spectrum(*load("Spektrum-glüh.txt"), edges)
benzene = bin_spectrum(*load("Spektrum-glüh_benzol.txt"), edges)
transmission = np.clip(100 * benzene / lamp, 0, 100)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6.5), sharex=True)

ax1.plot(centres, lamp, color="0.6", label="Tungsten lamp (reference)")
ax1.plot(centres, benzene, color="rebeccapurple", label="Through benzene (d = 20 mm)")
ax1.set_ylabel("Intensity / a.u.")
ax1.legend(loc="upper left")

ax2.plot(centres, transmission, color="rebeccapurple")
ax2.set_ylabel("Transmission / %")
ax2.set_xlabel(r"Wavenumber $\tilde{\nu}$ / cm$^{-1}$")
ax2.set_xlim(10000, 4000)
ax2.set_ylim(0, 110)
ax2.annotate("2nd overtone\nC–H stretch\n(≈ 1.14 µm)", xy=(8760, 5), xytext=(9350, 32),
             arrowprops=dict(arrowstyle="->", color="0.3"), ha="center")
ax2.annotate("1st overtone\nC–H stretch\n(≈ 1.67 µm)", xy=(6000, 5), xytext=(5200, 60),
             arrowprops=dict(arrowstyle="->", color="0.3"), ha="center")

top = ax1.secondary_xaxis("top", functions=(lambda k: 1e4 / k, lambda l: 1e4 / l))
top.set_xlabel(r"Wavelength $\lambda$ / µm")
for ax in (ax1, ax2):
    ax.grid(alpha=0.3)

fig.suptitle("Near-infrared transmission of benzene (FTIR)")
plt.tight_layout()
plt.savefig("../figures/benzene_transmission.png", dpi=150)
plt.show()
