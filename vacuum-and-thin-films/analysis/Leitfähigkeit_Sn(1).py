import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import FuncFormatter

data= pd.read_csv('sn beschichtung.csv',skiprows=1)

time=data['Time'].values
time=time-time[0]
rate=data['Inficon XTC/2 - Rate (COM9)'].values
dicke=data['Inficon XTC/2 - Thickness (COM9)'].values
resistance=data['Voltcraft VC8xx - Actual Value (COM7)'].to_numpy(copy=True)

mask_replace = (dicke < 0.55) & np.isinf(resistance)
resistance[mask_replace] = 1e8

mask_finite = np.isfinite(resistance)
resistance = resistance[mask_finite]
dicke = dicke[mask_finite]
ax = plt.gca()
ticks = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
labels = ['$10^3$', '$10^4$', '$10^5$', '$10^6$', '$10^7$', r'$\infty$']
ax.set_yticks(ticks)
ax.set_yticklabels(labels)
mask_0ohm = resistance >300
resistance=resistance[mask_0ohm]
dicke=dicke[mask_0ohm]

mask_fehler = ~((dicke > 0.83) & (resistance > 1000))
resistance=resistance[mask_fehler]
dicke=dicke[mask_fehler]

mask_messfehler= ~((dicke>0.5)&(resistance> 10**7))
resistance=resistance[mask_messfehler]
dicke=dicke[mask_messfehler]

mask_messfehler2= ~((dicke>0.59)&(resistance> 3*10**6))
resistance=resistance[mask_messfehler2]
dicke=dicke[mask_messfehler2]

dicke=100*dicke 
dicke=dicke/2.07 #falscher tooling faktor am anfang
dicke=dicke/2

plt.figure(figsize=(8, 6))
plt.plot(dicke,resistance,c='dimgrey',label='R(d)')
plt.yscale('log')

plt.axvspan(0, 12,color='#D60270', alpha=0.2, label='Bereich Ⅰ')
plt.axvspan(12, 15.5,color='#9B4F96', alpha=0.2, label=' Bereich Ⅱ')
plt.axvspan(15.5, dicke.max(),color='#0038A8', alpha=0.2, label='Bereich Ⅲ')
plt.xlim(left=0)

plt.xlabel(r'Schichtdicke d [$\mathrm{nm}$]') #dank tooling faktor einheit umbekannt bzw alles

plt.ylabel(r'Widerstand $R$ [$\Omega$]')
plt.legend(frameon=True, fancybox=False, edgecolor='black',facecolor='white')
plt.title(r'Widerstandsverlauf während der Sn-Bedampfung')
plt.grid(which='major', color='#AAAAAA', linewidth=0.8) 
plt.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)

ax = plt.gca()
ticks = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
labels = ['$10^3$', '$10^4$', '$10^5$', '$10^6$', '$10^7$', r'$\infty$']
ax.set_yticks(ticks)
ax.set_yticklabels(labels)
#plt.axhline(y=1e8, color='gray', linestyle='--', linewidth=2)#0.8

plt.tight_layout()

plt.savefig('Beschichtung1_Sn_R(d).pdf') 
plt.show()

