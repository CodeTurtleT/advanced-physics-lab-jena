import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

Minuten1=np.linspace(0, 12, 7)
Bronze1=np.array([232.6, 232.3, 232.1, 232.3, 232.5, 232.7, 233])
Zinn1=np.array([515, 508, 500, 499, 495, 493, 492 ])

Minuten2=np.linspace(0, 20, 11)
Kupfer2=np.array([137, 136.1, 135.2, 134.9, 134.3, 133.9,  133.7, 133.5, 133.3, 133.3, 133])
Bronze2=np.array([208.3, 201, 192.4, 187, 181.7, 178.4, 175, 172.1, 169.5, 167.5, 165.4])

fig, ax1 = plt.subplots(figsize=(8, 6))
fig.suptitle('Relaxation des elektrischen Widerstands')
#fig.suptitle('elektrischer Widerstand nach der Bedampfung')

l1=ax1.plot(Minuten1, Bronze1,marker='x', linestyle='-' ,label='Messung 1: Bronze R(t)', c='mediumseagreen')
l2=ax1.plot(Minuten2, Bronze2, marker='x', linestyle='-',label='Messung 2: Bronze R(t)', c='darkgreen')
l3=ax1.plot(Minuten2, Kupfer2,marker='x', linestyle='-', label='Messung 2: Kupfer R(t)', c='chocolate')
ax1.set_xlabel('Zeit t [min]')
ax1.set_ylabel(r'Widerstand R [$\Omega$]')
ax1.tick_params(axis='y')
ax1.grid(which='major', color='#AAAAAA', linewidth=0.8) 
ax1.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)
#ax1.set_xlim(left=0)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

ax2 = ax1.twinx()
l4=ax2.plot(Minuten1, Zinn1, marker='x', linestyle='-',label='Messung 1: Zinn R(t)',c='royalblue')
ax2.set_ylabel(r'Widerstand Zinn R [$\Omega$]',color='royalblue')
ax2.tick_params(axis='y')
ax2.grid(which='major', color='#AAAAAA', linewidth=0.8) 
ax2.grid(which='minor', color='#DDDDDD', linestyle='--', linewidth=0.5)

lines = l1 + l2 + l3 + l4
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right', frameon=True, fancybox=False, edgecolor='black', facecolor='white', framealpha=1)

plt.tight_layout()
#plt.savefig('Leitfähigkeit_Zeit.pdf') 
plt.show()
