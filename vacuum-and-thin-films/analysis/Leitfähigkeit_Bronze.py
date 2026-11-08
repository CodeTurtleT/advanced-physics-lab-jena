import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import FuncFormatter

data = pd.read_csv('bedampfung sn.csv', header=1)#hier ; als trnnzeichen

time=data['Time'].values
time=time-time[0]
dicke=data['Inficon XTC/2 - Thickness (COM9)'].values
resistance=data['Voltcraft VC8xx - Actual Value (COM7)'].values

mask = np.isfinite(resistance)

time = time[mask]
resistance = resistance[mask]
dicke = dicke[mask]

mask_bad = (resistance <= 200) | np.isnan(resistance)
resistance[mask_bad] = np.nan

#dicke = dicke * 100 

valid_R = resistance[~np.isnan(resistance)]
start_R = valid_R[0]
end_R = valid_R[-1]
delta_R = start_R - end_R

fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

ax1.plot(time, resistance, 'b.-', markersize=8, linewidth=1.5, label='Messdaten', c='dimgrey')

ax1.axvspan(11.95, 19.95, color='#9B4F96', alpha=0.2, label='Widerstandssprung der Bedampfungssphase')

text_str = (f'Start: $R_0 \\approx {start_R:.1f} \\,\\Omega$\n'
            f'Ende: $R_{{end}} \\approx {end_R:.1f} \\,\\Omega$\n'
            f'Abfall: $\\Delta R \\approx -{delta_R:.1f} \\,\\Omega$')

props = dict(boxstyle='square', facecolor='white', alpha=0.8, edgecolor='gray')
ax1.text(0.05, 0.1, text_str, transform=ax1.transAxes, fontsize=11,
        verticalalignment='bottom', bbox=props)

ax1.set_xlabel('Zeit $t$ [s]', fontsize=12)
ax1.set_ylabel(r'Widerstand $R$ [$\Omega$]', fontsize=12)
ax1.grid(which='major', color='#AAAAAA', linewidth=0.8) 
ax1.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)
ax1.legend(frameon=True, fancybox=False, edgecolor='black',facecolor='white', loc='upper right')
ax1.set_title(r'Verlauf des Widerstands während der Sn-Beschichtung auf Cu (Bronze)')

plt.tight_layout()
#plt.savefig('Beschichtung2_Bronze_R(d).pdf')
plt.show() 