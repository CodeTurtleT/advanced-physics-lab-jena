import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Turbo ohne Anfangsbereich.csv', skiprows=1)

#--------- DATEN SORTIEREN & FILTERN --------------
time = data['Time'].values
pressure = data['Leybold CM51 - Pressure TM1 (COM8)'].values

# 1. NaN entfernen
mask = np.isfinite(pressure)
pressure = pressure[mask]
time = time[mask]
time = time - time[0] # Start bei 0

# 4. Fit-Bereich (Tangente zwischen 10^1 und 10^3 mbar)
maske_tangente = (pressure <= 0.09) & (pressure > 0.0005)
pressure_fit = pressure[maske_tangente]
time_fit = time[maske_tangente]

#--------- FIT DURCHFÜHREN --------------
# Wir fitten ln(p) = ln(p0) - lambda * t
parameter, cov = np.polyfit(time_fit, np.log(pressure_fit), 1, cov=True)
m, b = parameter
dm, db = np.sqrt(np.diag(cov))

t_plot = np.linspace(time_fit.min(), time_fit.max(), 100)

fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

# Alle Daten
ax1.scatter(time, pressure, marker='x', s=20, alpha=0.4,
         color='hotpink', label='Messdaten (Pirani- Vakuumeter)')

ax1.semilogy(t_plot, np.exp(b + m* t_plot), '--',c='darkblue', label=(
        'Linearer Fit (Bereich konstantes S): '
        '\n'
        rf'$p(t) = m \cdot t + b$'
        '\n'
        rf'$m = ({m:.2e} \pm {dm:.1e})\,\mathrm{{mbar/s}}$'
        '\n'
        rf'$b = ({b:.2e} \pm {db:.1e})\,\mathrm{{mbar}}$'
    )
)
''
# Design
ax1.set_title('Abpumpkurve Turbopumpe')
ax1.set_xlabel('Zeit $t$ [s]', fontsize=12)
ax1.set_ylabel('Druck $p$ [mbar]', fontsize=12)
ax1.set_yscale('log')

# Grid
ax1.grid(which='major', color='#BBBBBB', linewidth=0.8) 
ax1.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)
ax1.minorticks_on()

# Legende
leg = ax1.legend(loc='upper right', frameon=True, fancybox=False, 
                 edgecolor='black', facecolor='white')

plt.tight_layout()
plt.savefig('Abpumpkurve_Turbo_Nenndrehzahl.pdf')
plt.show()