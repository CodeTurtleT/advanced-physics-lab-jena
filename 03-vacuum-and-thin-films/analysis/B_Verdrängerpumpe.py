import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data= pd.read_csv('Verdrängerpumpe.csv',skiprows=1)

print(data.head())
print(data.columns)

time=data['Time'].values
time=time-time[0]
pressure=data['Labovac PIZA 2000 - Pressure (COM6)'].values

def exp_decay(t, A, B, C):
    return np.exp(-A*t)*B +C
parameter, conv=curve_fit(exp_decay, time, pressure)
A, p_0, p_end=parameter
dA, dp_0, dp_end = np.sqrt(np.diag(conv))

A_sci = A * 1e3   
dA_sci = dA * 1e3

plt.figure(figsize=(10, 6))
plt.scatter(time, pressure, marker='x',s=20, alpha=0.5, label='Messdaten mit Membranvakuummeter', c='hotpink')
plt.plot(time, p_end + p_0 * np.exp(-A * time), 'k--', c='black',
    label=(
        'Exponentielle Anpassung: '
        rf'$p(t)=p_{{\mathrm{{end}}}} + p_0 \cdot e^{{-A\cdot t}}$'
        '\n'
        rf'$A=({A_sci:.2f} \pm {dA_sci:.2f}) \cdot 10^{{-3}}\,\mathrm{{s^{{-1}}}}$'
        '\n'
        rf'$p_{{\mathrm{{end}}}}=({p_end:.2f}\pm{dp_end:.2f})\,\mathrm{{mbar}},\; $'
        '\n'
        rf'$p_0=({p_0:.2f}\pm{dp_0:.2f})\,\mathrm{{mbar}}$'
    )
)

plt.xlabel('Zeit [s]')
plt.ylabel('Druck [mbar]')
leg = plt.legend(frameon=True,fontsize=12, fancybox=False,facecolor='white',edgecolor='black')
leg.get_frame().set_linewidth(0.8)

plt.title('Abpumpkurve Drehschieberpumpe')

#grid
plt.grid(which='major', color='#CCCCCC', linewidth=0.8) 
plt.grid(which='minor', color='#EEEEEE', linestyle='--', linewidth=0.5)
plt.minorticks_on()

#plt.savefig('Abpumpkurve_Drehschieberpumpe.pdf') 
plt.tight_layout()
plt.show()