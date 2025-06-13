# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:11:58 2021

@author: david
"""

import math
extrapolation = True # set this True to bypass the assert statements

T_melt = 3695 # K
dH_f = 52.3 # kJ/mol
W_M = 183.84 # g/mol


def specificHeatCapacity(tempK):
    """ Currently J/mol.K
    """
    if extrapolation == False:
        assert tempK >= 300, f'Input temperature for Specific Heat Capacity is out of range T >= 300 K'
    if tempK <= 3080:
        return (1 / W_M*1E+03) * 21.868372 + (8.068661 * 1E-03 * tempK) - (3.756196 * 1E-06 * 
                           math.pow(tempK, 2)) + (1.075862 * 1E-09 * 
                                   math.pow(tempK, 3)) + (1.406637 * 1E+04 / 
                                           math.pow(tempK, 2))
    elif tempK > 3080 and tempK <= 3695:
        return (1 / W_M*1E+03) * 2.022 + (1.315E-02 * tempK)
    elif tempK > 3695:
        return (1 / W_M*1E+03) * 51.3
    else:
        print(f'Something went wrong! T = {tempK}')
        return 0
    
def thermalConductivity(tempK):
    """ W/m.K
    """
    if extrapolation == False:
        assert tempK >= 300 and tempK <= 6000, f'Input temperature for Specific Heat Capacity is out of range T >= 300 K'
    if tempK <= 3695:
        return 149.441 - (45.466E-03 * tempK) + (13.193E-06 * 
                         math.pow(tempK, 2)) - (1.484E-09 * 
                                 math.pow(tempK, 3)) + (3.866E+06 / 
                                         math.pow(tempK, 2))
    elif tempK > 3695 and tempK <= 6000:
        return 66.6212 + (0.02086 * (tempK - T_melt)) - (3.7585E-06 * 
                         math.pow((tempK - T_melt), 2))   
    else:
        print(f'Something went wrong! T = {tempK}')
        return 0
    
def density(tempK):
    """ g/cm^3 * by 1000 for kg/m^3
    """
    T_0 = 293.15 # K
    if extrapolation == False:
        assert tempK >= 300 and tempK <= 6000, f'Input temperature for Specific Heat Capacity is out of range T >= 300 K'
    if tempK <= 3695:
        return 1E+03 *19.25 - (2.66207E-04 * (tempK - T_0)) - (3.0595E-09 * 
                       math.pow((tempK - T_0), 2)) - (9.5185E-12 * 
                               math.pow((tempK - T_0), 3))
    elif tempK > 3695 and tempK <= 6000:
        return 1E+03 * 16.267 - (7.679E-04 * (tempK - T_melt)) - (8.091E-08 * 
                        math.pow((tempK - T_melt), 2))
    else:
        print(f'Something went wrong! T = {tempK}')
        return 0
    
def electricalResistivity(tempK):
    """
    

    Parameters
    ----------
    temp_K : TYPE
        DESCRIPTION.

    Returns
    -------
    electricalResistivity : TYPE
        DESCRIPTION.

    """
    electricalResistivity = 1E-08 * (-0.9680 +1.9274E-02 * tempK + 7.8260E-06 * math.pow(tempK, 2) - 1.8517E-09 * math.pow(tempK, 3) + 2.0790E-13 * math.pow(tempK, 4))

    return electricalResistivity

def electricalConductivity(tempK):
    """
    

    Parameters
    ----------
    temp_K : TYPE
        DESCRIPTION.

    Returns
    -------
    electricalConductivity : TYPE
        DESCRIPTION.

    """
    electricalConductivity = 0.97E+06
    return electricalConductivity

                                   
                