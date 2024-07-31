import pandas as pd
import PyCO2SYS as pyco2

from calc_random_data import calc_rnd_data
from random_generators import random_normal
from calc_eq_constants import calc_pKB_STP
from calc_d11B_borate import calc_d11B_borate
from calc_pH_TS import calc_pH_TS
from klochko_consts import alpha_B3B4, epsilon_B3B4

def compute_walk(data, C, M, C_SD, M_SD):
    
    # Generate random data input table and random constants for calibration equation           
    data_rnd = calc_rnd_data(data)
    C_rnd = random_normal(C, C_SD, 'absolute')
    M_rnd = random_normal(M, M_SD, 'absolute')
    
    # Temporary storage lists
    tmp_list_pKB = []
    tmp_list_borate = []
    tmp_list_pH = []
    tmp_list_pCO2 = []
    
    # Loop to iterate over all time/depths in the data table
    for P, dBf, T, S, dBsw, Alk in zip(data_rnd['Pressure'], data_rnd['d11B_f_rnd'], data_rnd['Temperature_rnd'], data_rnd['Salinity_rnd'], data_rnd['d11B_sw_rnd'], data_rnd['Alkalinity_rnd']):
        tmp_pKB = calc_pKB_STP(T, S, P)
        tmp_d11B_borate = calc_d11B_borate(dBf, C_rnd, M_rnd)
        tmp_pH = calc_pH_TS(tmp_d11B_borate, dBsw, tmp_pKB, alpha_B3B4, epsilon_B3B4)
        
        # PyCO2SYS arguments: known ALK and pH
        kwargs = {
            "par1": Alk,
            "par2": tmp_pH,
            "par1_type": 1,
            "par2_type": 3,
            "temperature": T,
            "salinity": S
        }
        
        # Normal way to run PyCO2SYS
        res_pyco2 = pyco2.sys(**kwargs)
        
        # Append results to temporary lists
        tmp_list_pKB.append(tmp_pKB)
        tmp_list_borate.append(tmp_d11B_borate)
        tmp_list_pH.append(tmp_pH)
        tmp_list_pCO2.append(res_pyco2["pCO2"])
            
    # Create data frame for storage
    walk_out = pd.DataFrame()
    walk_out['Time'] = data['Time']
    walk_out['pKB'] = tmp_list_pKB
    walk_out['d11B_borate'] = tmp_list_borate
    walk_out['pH'] = tmp_list_pH
    walk_out['pCO2'] = tmp_list_pCO2
    
    #MC_list_pH.append(walk_out['pH'])
    #MC_list_pCO2.append(walk_out['pCO2'])
    return walk_out['pH'], walk_out['pCO2']