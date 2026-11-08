import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data= pd.read_csv('20 Minuten Aufnashme.csv',skiprows=1)

def sekunden_zu_minuten(x, pos):
    return f'{x/60:.0f}'

def mbar_zu_milli_mbar(y, pos):
    return f'{y*1e3:.0f}'

time=data['Time'].values
time=time-time[0]
pressure_tm1=data['Leybold CM51 - Pressure TM1 (COM8)'].values
pressure_pm=data['Leybold CM51 - Pressure PM (COM8)'].values

plt.figure(figsize=(10, 6))

plt.axvspan(0, 93,color='hotpink', alpha=0.2, label='Abpumpvorgang')
plt.axvspan(374, 1330,color='steelblue', alpha=0.2, label='für Dichtheitbestimmung relevanter Bereich')

plt.plot(time, pressure_tm1, label='Messdaten mit Pirani- Vakuumeter', c='peru')
plt.plot(time, pressure_pm,label='Messdaten mit Penning- Vakuumeter', c='mediumseagreen')
plt.xlabel('Zeit (s)')
plt.ylabel('Druck')
plt.title('Druckanstieg im geschlossenen Rezipienten über 20 Minuten')
plt.legend(loc='upper right', frameon=True, fancybox=False, edgecolor='black',facecolor='white')
plt.grid(which='major', color='#AAAAAA', linewidth=0.8) 
plt.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)

plt.gca().xaxis.set_major_formatter(FuncFormatter(sekunden_zu_minuten))
plt.xlabel('Zeit [min]')

plt.gca().yaxis.set_major_formatter(FuncFormatter(mbar_zu_milli_mbar))
plt.ylabel(r'Druck [$10^{-3}$ mbar]')

#plt.savefig('Druckanstieg_20Min.pdf') 
plt.show()
