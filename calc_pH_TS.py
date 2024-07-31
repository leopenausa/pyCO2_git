import math

def calc_pH_TS(d11B_brte, d11B_sw, pKB_STP, alpha, epsilon):
    '''A function to calculate pH from d11B borate, d11Bsw and equilibrium constants'''
    
    pH_TS = pKB_STP - math.log10(-(d11B_sw - d11B_brte) / (d11B_sw - alpha * d11B_brte - epsilon))
    
    return pH_TS