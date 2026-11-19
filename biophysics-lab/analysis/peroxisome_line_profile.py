#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 20:07:32 2025

@author: trinity
"""

import pandas as pd
import matplotlib.pyplot as plt

# CSV einlesen mit Semikolon als Trennzeichen
data = pd.read_csv("konfokal_perxisiom.csv", sep=';')

# Spalten prüfen
print(data.columns.tolist())

# Spalten auslesen
distance = data["Distance_(micros)"].values
gray_value = data["Gray_Value"].values
x_fit = data["X_Fit:_Gaussian"].values
y_fit = data["Fit:_Gaussian"].values

# Plot
plt.plot(distance, gray_value, label='Intensität', color='black', linestyle='-', marker='o')
plt.plot(x_fit, y_fit, label='Gauß-Fit', color='blue', linestyle='--')

plt.legend()
plt.xlabel('Distanz (micros)')
plt.ylabel('Intensität (Gray Value)')
plt.grid(True)
plt.savefig("../figures/peroxisome_line_profile.png", dpi=200)
plt.show()
