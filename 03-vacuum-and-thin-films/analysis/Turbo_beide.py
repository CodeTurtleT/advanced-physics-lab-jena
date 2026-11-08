import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
#mit hichfahren=1
#schon 2700 =2

data1= pd.read_csv('Turbo mit Übergangsbereich.csv',skiprows=1)

time1=data1['Time'].values
time1=time1-time1[0]
pressure1_tm1=data1['Leybold CM51 - Pressure TM1 (COM8)'].values
pressure1_pm=data1['Leybold CM51 - Pressure PM (COM8)'].values

data2= pd.read_csv('Turbo ohne Anfangsbereich.csv',skiprows=1)

time2=data2['Time'].values
time2=time2-time2[0]
pressure2_tm1=data2['Leybold CM51 - Pressure TM1 (COM8)'].values
pressure2_pm=data2['Leybold CM51 - Pressure PM (COM8)'].values

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True) #erstmal nebeneunadner
fig.suptitle('Vergleich der Abpumpkurven der Turbomolekularpumpe', fontsize=16)# fontweight='bold'

ax1.plot(time1, pressure1_tm1, label='Messdaten mit Pirani- Vakuumeter', c='royalblue')
ax1.plot(time1, pressure1_pm, label='Messdaten mit Penning- Vakuumeter', c='tomato')
ax1.set_title('Mit Hochlaufphase (variables Saugvermögen)')
ax1.set_xlabel('Zeit [s]')
ax1.set_ylabel('Druck [mbar]')
ax1.set_yscale('log')  # logarithmische y-Achse
ax1.grid(which='major', color='#CCCCCC', linewidth=0.8) 
ax1.grid(which='minor', color='#EEEEEE', linestyle='--', linewidth=0.5)
ax1.minorticks_on()
leg = ax1.legend(loc='upper right', frameon=True, fancybox=False,facecolor='white', edgecolor='black')
leg.get_frame().set_linewidth(0.8)

#plot 2
ax2.plot(time2, pressure2_tm1, label='Messdaten mit Pirani- Vakuumeter', c='royalblue')
ax2.plot(time2, pressure2_pm, label='Messdaten mit Penning- Vakuumeter', c='tomato')
ax2.set_title('Bei Nenndrehzahl (konstantes Saugvermögen)')
ax2.set_xlabel('Zeit [s]')
ax2.set_ylabel('Druck [mbar]')
ax2.set_yscale('log')
ax2.grid(which='major', color='#CCCCCC', linewidth=0.8) 
ax2.grid(which='minor', color='#EEEEEE', linestyle='--', linewidth=0.5)
ax2.minorticks_on()
leg = ax2.legend(loc='lower left', frameon=True, fancybox=False,facecolor='white', edgecolor='black')
leg.get_frame().set_linewidth(0.8)

plt.tight_layout()
#plt.savefig('Turbo_Vergleich.pdf')
plt.show()