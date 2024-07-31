import numpy as np
import pandas as pd
from random_generators import random_normal

# Vectorization of of calculations with numpy provides a 10-fold improvement in speed.
# It can probably be tunned even further by elimination pandas in this function and working
# exclusively with numpy arrays

def calc_rnd_data(data):
    ''' Generate a random data matrix from input data uncertainties'''
    
    # Create dataframe to store results
    data_rnd = pd.DataFrame()
    
    data_rnd['Time'] = data['Time']
    data_rnd['Pressure'] = data['Pressure']
    
    # d11B_forams
    d11B_f = np.array([data['d11B_foram'], data['2SD_d11Bf']])
    d11B_f_res = np.apply_along_axis(random_normal, 0, d11B_f[0], d11B_f[1], 'absolute')
    data_rnd['d11B_f_rnd'] = pd.Series(d11B_f_res)
    
    # Temperatures
    SST_f = np.array([data['Temperature'], data['2SD_temp']])
    SST_f_res = np.apply_along_axis(random_normal, 0, SST_f[0], SST_f[1], 'absolute')
    data_rnd['Temperature_rnd'] = pd.Series(SST_f_res)
    
    # Salinities
    Sal_f = np.array([data['Salinity'], data['2SD_sal']])
    Sal_f_res = np.apply_along_axis(random_normal, 0, Sal_f[0], Sal_f[1], 'absolute')
    data_rnd['Salinity_rnd'] = pd.Series(Sal_f_res)
    
    # d11B seawater
    d11B_sw = np.array([data['d11B_sw'], data['2SD_d11Bsw']])
    d11B_sw_res = np.apply_along_axis(random_normal, 0, d11B_sw[0], d11B_sw[1], 'absolute')
    data_rnd['d11B_sw_rnd'] = pd.Series(d11B_sw_res)
    
    # Alkalinity
    Alk_f = np.array([data['alkalinity'], data['2SD_alk']])
    Alk_f_res = np.apply_along_axis(random_normal, 0, Alk_f[0], Alk_f[1], 'absolute')
    data_rnd['Alkalinity_rnd'] = pd.Series(Alk_f_res)
    
    return data_rnd