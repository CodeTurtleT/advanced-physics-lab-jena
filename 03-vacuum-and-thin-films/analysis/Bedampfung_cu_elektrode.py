import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv('bedampfung elektroden cu.csv',skiprows=1)

time=data['Time'].values
time=time-time[0]
thickness=data['Inficon XTC/2 - Thickness (COM9)'].values
rate=data['Inficon XTC/2 - Rate (COM9)'].values

thickness=100*thickness 
rate=rate/10

fig, ax1=plt.subplots(figsize=(8, 6))
fig.suptitle('Bedampfungsprozess der Cu-Elektroden')

ax1.plot(time, thickness, label='Dicke d(t)',c='chocolate')
ax1.set_ylabel('Schichtdicke $d$ [nm]',c='chocolate')

ax2 = ax1.twinx()
ax2.plot(time, rate, label='Rate', c='dimgrey')
ax2.set_ylabel('Rate $r$ [nm/s]',c='dimgrey')
ax1.set_xlabel('Zeit t [s]')

ax2.grid(which='major', color='#AAAAAA', linewidth=0.8) 
ax2.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(lines1 + lines2, labels1 + labels2, frameon=True, fancybox=False, edgecolor='black', facecolor='white')

plt.tight_layout()

#plt.savefig('Bedampfung_CU_Elektrode.pdf') 
plt.show()

