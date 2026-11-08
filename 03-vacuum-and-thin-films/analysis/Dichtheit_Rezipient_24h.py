import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

#----------------BEIDES-------------------------------------
def sekunden_zu_minuten(x, pos):
    return f'{x/60:.0f}'

def sekunden_zu_stunden(x, pos):
    return f'{x/3600:.0f}'

def mbar_zu_milli_mbar(y, pos):
    return f'{y*1e3:.0f}'

data= pd.read_csv('20 Minuten Aufnashme.csv',skiprows=1)

time=data['Time'].values
time=time-time[0]
pressure_tm1=data['Leybold CM51 - Pressure TM1 (COM8)'].values
pressure_pm=data['Leybold CM51 - Pressure PM (COM8)'].values

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12) ) #erstmal nebeneunadner sharey=True
fig.suptitle('Druckanstieg im geschlossenen Rezipienten', fontsize=16)# fontweight='bold'

#----------------PLOT LINKS-------------------------------------
maske = time >= 370
time = time[maske]
pressure_pm = pressure_pm[maske]

maske2= time <=610
time = time[maske2]
pressure_pm = pressure_pm[maske2]
time=time-time[0]

coeffs, cov = np.polyfit(time, pressure_pm, 1, cov=True)
dm, db = np.sqrt(np.diag(cov))
fit_pressure=np.poly1d(coeffs)
time_fit=np.linspace(0,250, 1000)

ax1.scatter(time, pressure_pm, marker='o',s=10, alpha=0.5, label='Messdaten mit Penning- Vakuumeter', c='mediumseagreen')
ax1.plot(time_fit, fit_pressure(time_fit), '--',c='darkblue',label=(
        'Linearer Fit: 'rf'$p(t) = m \cdot t + b$'
        '\n'
        rf'$m = ({coeffs[0]:.3e} \pm {dm:.1e})\,\mathrm{{mbar/s}}$'
        '\n'
        rf'$b = ({coeffs[1]:.3e} \pm {db:.1e})\,\mathrm{{mbar}}$'
    )
)

ax1.set_xlabel('Zeit [s]')
ax1.set_ylabel(' Druck [mbar]')
ax1.legend(frameon=True, fancybox=False, edgecolor='black',facecolor='white')
ax1.set_title('Beobachtung nach Abpumpen')
ax1.grid(which='major', color='#AAAAAA', linewidth=0.8) 
ax1.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)

ax1.xaxis.set_major_formatter(FuncFormatter(sekunden_zu_minuten))
ax1.set_xlabel('Zeit [min]')
ax1.yaxis.set_major_formatter(FuncFormatter(mbar_zu_milli_mbar))
ax1.set_ylabel(r'Druck [$10^{-3}$ mbar]')

#----------------PLOT RECHTS-------------------------------------
time_24h=np.append(time, 86400)#nach 24h
pressure_pm_24h=np.append(pressure_pm, 0.606)

coeffs2, cov2 = np.polyfit(time_24h, pressure_pm_24h, 1, cov=True)
dm2, db2 = np.sqrt(np.diag(cov2))
fit_pressure_24h=np.poly1d(coeffs2)
time_fit_24h=np.linspace(0,86500, 10000)

ax2.scatter(time_24h, pressure_pm_24h, marker='o',s=10, alpha=0.5, label='Messdaten links + 24h mit Pirani- Vakuumeter', c='mediumseagreen')
ax2.plot(time_fit_24h, fit_pressure(time_fit_24h), '--',c='darkblue')
ax2.plot(time_fit_24h, fit_pressure_24h(time_fit_24h), '--',c='hotpink',label=(
        'Linearer Fit 24h: 'rf'$p(t) = m \cdot t + b$'
        '\n'
        rf'$m = ({coeffs2[0]:.3e} \pm {dm2:.1e})\,\mathrm{{mbar/s}}$'
        '\n'
        rf'$b = ({coeffs2[1]:.3e} \pm {db2:.1e})\,\mathrm{{mbar}}$'
    )
)

ax2.set_xlabel('Zeit [s]')
ax2.set_ylabel(' Druck [mbar]')
ax2.legend(frameon=True, fancybox=False, edgecolor='black',facecolor='white')
ax2.set_title('Beobachtung nach 24 Stunden')
ax2.grid(which='major', color='#AAAAAA', linewidth=0.8) 
ax2.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)

ax2.xaxis.set_major_formatter(FuncFormatter(sekunden_zu_stunden))
ax2.set_xlabel('Zeit [h]')
ax2.yaxis.set_major_formatter(FuncFormatter(mbar_zu_milli_mbar))
ax2.set_ylabel(r'Druck [$10^{-3}$ mbar]')

#----------------BEIDES-------------------------------------
plt.tight_layout()
#plt.savefig('Druckanstieg_24h2.pdf') 
plt.show()