import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data= pd.read_csv('vorpumpe.csv',skiprows=1)

#--------- DATEN SORTIEREN--------------
time=data['Time'].values
pressure=data['Labovac PIZA 2000 - Pressure (COM6)'].values

mask = np.isfinite(pressure)
pressure = pressure[mask]
time = time[mask]
time = time - time[0]

maske2= time >=33
pressure = pressure[maske2]
time = time[maske2]
time = time - time[0]

maske3= time <=150
pressure = pressure[maske3]
time = time[maske3]

pressure_tangente = pressure
time_tangente = time
maske_tangente = (pressure_tangente <= 10**3) & (pressure_tangente >= 10**1)
pressure_tangente = pressure_tangente[maske_tangente]
time_tangente = time_tangente[maske_tangente]

parameter, cov = np.polyfit(time_tangente, np.log(pressure_tangente), 1, cov=True)
m, b = parameter
dm, db= np.diag(cov)
tangente = np.poly1d(parameter)
t_plot = np.linspace(time_tangente.min(), time_tangente.max(), 100)

plt.figure(figsize=(10, 6))
plt.scatter(time, pressure, marker='x', s=30, alpha=0.5, label='Messdaten mit Membranvakuummeter', c='hotpink')
plt.semilogy(t_plot, np.exp(b + m* t_plot), '--',c='darkblue', label=(
        'Linearer Fit (Bereich konstantes S): '
        '\n'
        rf'$p(t) = m \cdot t + b$'
        '\n'
        rf'$m = ({m:.2e} \pm {dm:.1e})\,\mathrm{{mbar/s}}$'
        '\n'
        rf'$b = ({b:.2e} \pm {db:.1e})\,\mathrm{{mbar}}$'
    )
)

plt.xlabel('Zeit [s]')
plt.ylabel('Druck [mbar]')
plt.legend(frameon=True, fancybox=False, edgecolor='black',facecolor='white')
plt.grid(which='major', color='#AAAAAA', linewidth=0.8) 
plt.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)

plt.title('Abpumpkurve Drehschieberpumpe')

#grid
plt.grid(which='major', color='#CCCCCC', linewidth=0.8) 
plt.grid(which='minor', color='#EEEEEE', linestyle='--', linewidth=0.5)
plt.minorticks_on()

plt.tight_layout()
#plt.savefig('Abpumpkurve_Drehschieberpumpe_ln.pdf') 

plt.show()