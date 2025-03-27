# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 18:15:48 2025

@author: andre
"""

import numpy as np
import math

#FORMULA SEMI EMPIRICA DE LA MASSA
def B(Z,A):
    a_v=15.56
    a_s=17.23
    a_c=0.697
    a_a=23.285
    a_p=12
    def d(Z,A):
        if A % 2 == 0:
            if Z % 2 == 0:
                return a_p/(np.sqrt(A))
            else:
                return -a_p/np.sqrt(A)
        else:
            return 0
        
    return a_v*A - a_s*(A**(2/3)) - a_c*(Z**2)/(A**(1/3)) - a_a*(2*Z-A)**2/A + d(Z,A)

#MASSA ATÒMICA
#usant 1Da=931.5MeV/c2

def m(Z,A):
    m_H = 1.007825 #Da
    M_N = 1.00866501 #Da
    return Z*m_H + (A-Z)*M_N - (B(Z,A)/931.502)

#Energies d'enllaç en MeV
elements=["d", "t","Heli 3","Heli 4"]
energies_calc=[B(1,2),B(1,3),B(2,3),B(2,4)]
energies_tab=[2.2245, 8.4820, 7.7186, 28.2970]
diferencies=[]
errors=[]

for j in range(4):
    diferencies.append(np.abs(energies_tab[j] - energies_calc[j]))
    errors.append((np.abs(energies_tab[j] - energies_calc[j]))*100/energies_tab[j])
    
print("Element", "Energia tab", "Energia calc", "Error %")
for i in range(4):
    print(elements[i], energies_tab[i], energies_calc[i], errors[i])

#BALANÇ ENERGETIC EN MeV
Q_1 = B(2,3)-2*B(1,2)
Q_2 = B(2,4)-B(1,2)-B(1,3)

Q=[Q_1,Q_2]
Q_tab=[3.269, 17.59]
difQ=[]
errQ=[]
for j in range(2):
    difQ.append(np.abs(Q[j] - Q_tab[j]))
    errQ.append((np.abs(Q[j] - Q_tab[j]))*100/Q_tab[j])

print("Reaccio", "Q tab", "Q calc", "Error %")
for i in range(2):
    print([i+1],Q_tab[i],Q[i],errQ[i])

    
    
    