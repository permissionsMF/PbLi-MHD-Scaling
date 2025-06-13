# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:48:02 2021

@author: dhorsley
Title: Property Correlations for PB 17.0 at.% Li
Name: prop_correlations_Pb17at.Li.py
Description: A module of functions to return material properties. Property 
correlations included are:
    1. Density
    2. Spcific Heat Capacity
    3. Thermal Diffusivity
    4. Thermal Conductivity
    5. Dynamic Viscosity
    6. Volumetric Thermal Expansion Coefficient
    7. Surface Tension
    8. Electrical Resistivity
    9. Vapour Pressure
    10. Speed of Sound
    
Reference: LM-D-R-262 - Literature review of PbLi properties, 
ENEA [27/04/2107] - IDM

Notes:
    1. Add logging to flag warnings when required temperture is out of the 
    correlation range. Then allow return of values, but with extrapolation
    warning.
"""
import math
from scipy import constants as const



def density(tempK):
    """ Returns the density of Pb %at.17 Li for a given temperature
    in degrees Kelvin. Correlation has 0.3% error and 4.39% scattering.
    Valid for temperature within the 508 - 880 K range.
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which density is required
    Returns:
        density [kg/m^3] float: temperature dependant density for
        Pb 17.0at.% Li.
    """
    #assert tempK >= 508 and tempK <= 880, "Input temperature for density is \
    #                                        out of range (508 <= T <= 880 K)"
    return 10520.35 - (1.19051 * tempK)

def specificHeat(tempK):
    """ Returns the specific heat capacity Cp for Pb 16.8at.% Li for a given
    temperature in degrees Kelvin. Correlation has an +/- 3% error and a 
    31.39% scattering. It is valid for the temperatures within the 
    range 505 - 880 K.
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which specific heat capacity is required
    Returns:
        specficHeatCapacity [J/(g.K)] float: temperature dependant specific 
        heat capacity
    """
    assert tempK >= 508 and tempK <= 880, f"Input temperature for Specific Heat\
                                             capacity, C_p is out of range \
                                             (508 <= T <= 880 K). T={tempK} K"
    return 0.195 - (tempK * 9.116E-06)

def thermalDiffusivity(tempK):
    """ Returns the thermal diffusivity, alpha, for Pb 17.0at.% Li for a given
    temperature in degrees Kelvin. Correlation has an error <=5E-03 cm^2/s and\
    a 37.35% scattering. It is valid for the temperatures within the 
    range 505 - 773 K.
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which thermal diffusivity is required
    Returns:
        thermalDiffusivity [cm^2/s] float: temperature dependant thermal 
        diffusivity
    """
    assert tempK >= 508 and tempK <= 773, "Input temperature for thermal\
                                             diffusivity, alpha is out of range \
                                             (508 <= T <= 773 K)"
    return tempK * 3.46E-04 - 1.05E-01

def thermalConductivity(tempC):
    """ Returns the thermal conductivity, lambda, for Pb 17.0at.% Li for a 
    given temperature in degrees Celsius. Correlation has an 37.72% scattering.
    It is valid for the temperatures within the range 505 - 873 K.
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempC [C] float: temperature at which thermal conductivity is required
    Returns:
        thermalConductivity [W/cm.K] float: temperature dependant thermal 
        conductivity
    """
    assert tempC >= 508 and tempC <= 873, "Input temperature for thermal conductivity, lambda is out of range 508 <= T <= 873 K)"
    return 0.1451 + (tempC * 1.9631E-04)

def dynamicViscosity(tempK):
    """ Returns the dynamic viscosity, mew, for Pb 16.8at.% Li for a 
    given temperature in degrees Kelvin. Correlation has an 14.75% scattering.
    It is valid for the temperatures within the range 508 - 625 K.
    Dependancies:
        1. math
        2. scypy.constants
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which Dynamic Viscosity is required
    Returns:
        dynamicViscosity [mPa.s] float: temperature dependant dynamic viscosity
    """
    #assert tempK >= 508 and tempK <= 625, "Input temperature for Dynamic \
    #                                        Viscosity, mew is out \
    #                                        of range 508 <= T <= 625 K"
    return 0.187 * math.exp(11640 / (const.R * tempK)) * 1E-03

def kinematicViscosity(tempK):
    return dynamicViscosity(tempK) / density(tempK)

def volumetricThermalExpansionCoeff(tempK):
    """ Returns the Volumetric Thermal Expansion Coefficient, beta, for 
    Pb 17.0at.% Li for a given temperature in degrees Kelvin. Correlation has 
    an 3% error and a 49.41% scattering. It is valid for the temperatures 
    within the range 508 - 880 K.
    Dependancies:
        1. NA
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which Volumetric Thermal Expansion 
        Coefficient is required
    Returns:
        volumetricThermalExpansionCoeff [1/K] float: temperature dependant 
        Volumetric Thermal Expanison Coefficient
    """
    assert tempK >= 508 and tempK <= 880, "Input temperature for Volumetric Thermal Expansion Coefficient, beta, is out of range 508 <= T <= 880 K"
    return (11.221 + (tempK * 1.531E-03)) * 1E-05

def surfaceTension(tempK):
    """ Returns the Surface Tension, sigma, for Pb 17.0at.% Li for a given 
    temperature in degrees Kelvin. Correlation has an 2% error and a 15.08% 
    scattering. It is valid for the temperatures within the range 508 - 700 K.
    Dependancies:
        1. NA
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which the Surface Tension is required
    Returns:
        surfaceTension [mN/m] float: temperature dependant Surface Tension
    """
    assert tempK >= 508 and tempK <= 700, "Input temperature for Surface Tension, sigma, is out of range 508 <= T <= 700 K"
    return 459.4 - (0.04 * (tempK - 518))

def electricalResistivity(tempK):
    """ Returns the Electrical Resistivity, rho_el, for Pb 17.0at.% Li for a 
    given temperature in degrees Kelvin. Correlation has a 11.83% scattering. 
    It is valid for the temperatures within the range 600 - 800 K.
    Dependancies:
        1. math
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempK [K] float: temperature at which the Electrical Resistivity is 
        required
    Returns:
        electricalResistivty [ohm/m] float: temperature dependant Electrical
        Resistivity.
    """
    #assert tempK >= 600 and tempK <= 800, "Input temperature for Electrical Resistivity correlation is out of range 600 <= T <= 800 K"
    return 103.33E-08 - (tempK * 6.750E-11) + (math.pow(tempK, 2) * 4.180E-13)

def electricalConductivity(tempK):
    return 1 / electricalResistivity(tempK)

def vapourPressure(tempC):
    """ Returns the Vapour Pressure, P_V, for Pb 17.0at.% Li for a given 
    temperature in degrees Celsuis. Correlation has no recorded error or 
    scattering data. It is valid for the temperatures within the 
    range 508 - 873 K.
    Dependancies:
        1. math
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempC [C] float: temperature at which the Vapour Pressure is required
    Returns:
        vapourPressure [mbar] float: temperature dependant Vapour Pressure
    """
    assert tempC >= 508 and tempC <= 873, "Input temperature for Vapour Pressure correlation is out of range 508 <= T <= 873 K"
    return math.pow(tempC, 20.025) * 1.4508E-59

def speedOfSound(tempC):
    """ Returns the Speed of Sound, c, for Pb 17.0at.% Li for a given 
    temperature in degrees Celsuis. Correlation has a reported error 
    of +/- 7 m/s. It is valid for the temperatures within the 
    range 513 - 783 K.
    Dependancies:
        1. NA
    Notes:
        1. NA
    Ref.:
        1. As above
    Params.:
        tempC [C] float: temperature at which the Speed of Sound is required
    Returns:
        speedOfSound [m/s] float: temperature dependant Speed of Sound
    """
    assert tempC >= 513 and tempC <= 783, "Input temperature for Speed of Sound correlation is out of range 513 <= T <= 783 K"
    return 1876 - (0.306 * tempC)
    