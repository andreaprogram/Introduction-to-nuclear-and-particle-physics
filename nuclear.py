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

elements=["Carboni 12", "Alumini 27","Estronci 88","Reni 185","Urani 238"]
masses_calc=[m(6,12), m(13,27), m(38,88), m(75,185), m(92,238)]
masses_tab=[12.000000, 26.981539, 87.905619, 184.952951, 238.050785]
diferencies=[]
errors=[]

for j in range(5):
    diferencies.append(np.abs(masses_tab[j] - masses_calc[j]))
    errors.append((np.abs(masses_tab[j] - masses_calc[j]))*100/masses_tab[j])
    
print("Element", "Massa tab", "Massa calc", "Error %")
for i in range(5):
    print(elements[i], masses_tab[i], masses_calc[i], errors[i])


    
    
    