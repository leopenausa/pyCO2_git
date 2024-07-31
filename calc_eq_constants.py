import math
import numpy as np

# Following Zeebe & Wolf-Gladrow (2001) we create functions to calculate intermediate equilibrium constant parameters. 
# KB(S, T) (Dickson, 1990) and pressure effects on equilibrium constants according to Millero (1995)

def calc_KB_ST(T, S):
    ''' Compute KB constant from temperature and Salinity'''
    
    # Temp to Kelvin
    T_K = T + 273.15
    
    # LnKB/k0
    LnKBk0 = (-8966.9 - 2890.53 * S ** (0.5) - 77.942 * S + 1.728 * S ** (1.5) - 0.0996 * S ** (2)) /\
    T_K + (148.0248 + 137.1942 * S ** (0.5) + 1.62142 * S) + (-24.4344 - 25.085 * S ** (0.5) - 0.2474 * S) * np.log(T_K) + 0.053105 * S ** (0.5) * T_K
    
    # KB
    KB = np.exp(LnKBk0)
    
    return KB

def calc_DeltaVi(T):
    a0 = -29.48
    a1 = 0.1622
    a2 = -0.002608
    
    DVi = a0 + a1 * T + a2 * T ** 2
    
    return DVi

def calc_DeltaKi(T):
    b0 = -0.00284
    b1 = 0
    b2 = 0
    
    DKi = b0 + b1 * T + b2 * T ** 2
    
    return DKi

def calc_pKB_STP(T, S, P):
    
    R = 83.144621     # NIST CODATA (2010)  cm3 bar mol-1 K-1
    
    # Temp to Kelvin
    T_K = T + 273.15
    
    LN_KBP_KB0 = -(calc_DeltaVi(T) / (R * T_K)) * P + (0.5 * calc_DeltaKi(T) / (R * T_K)) * P ** 2
    KBP_KB0 = np.exp(LN_KBP_KB0)
    
    KB_STP = KBP_KB0 * calc_KB_ST(T, S)
    
    pKB_STP = - math.log10(KB_STP)
    
    return pKB_STP