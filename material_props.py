import numpy as np
from scipy.interpolate import interp1d

# Data for PbLi properties as a function of temperature (Celsius)
# Values are approximate and for demonstration only.

_T_C = np.array([300, 400, 500, 550])

_sigma = np.array([1.0e6, 0.95e6, 0.90e6, 0.87e6])  # electrical conductivity, S/m
_rho = np.array([9420, 9300, 9180, 9120])           # density, kg/m^3
_mu = np.array([2.5e-3, 2.0e-3, 1.7e-3, 1.5e-3])   # dynamic viscosity, Pa*s
_k = np.array([15.0, 16.0, 17.0, 17.5])            # thermal conductivity, W/m/K
_beta = np.array([1.1e-4, 1.15e-4, 1.20e-4, 1.23e-4])  # thermal expansion, 1/K

_sigma_interp = interp1d(_T_C, _sigma, fill_value="extrapolate")
_rho_interp = interp1d(_T_C, _rho, fill_value="extrapolate")
_mu_interp = interp1d(_T_C, _mu, fill_value="extrapolate")
_k_interp = interp1d(_T_C, _k, fill_value="extrapolate")
_beta_interp = interp1d(_T_C, _beta, fill_value="extrapolate")

def sigma(T_C):
    """Electrical conductivity as a function of temperature in Celsius."""
    return float(_sigma_interp(T_C))

def rho(T_C):
    """Density as a function of temperature in Celsius."""
    return float(_rho_interp(T_C))

def mu(T_C):
    """Dynamic viscosity (Pa*s) as a function of temperature in Celsius."""
    return float(_mu_interp(T_C))

def k(T_C):
    """Thermal conductivity as a function of temperature in Celsius."""
    return float(_k_interp(T_C))

def beta(T_C):
    """Thermal expansion coefficient as a function of temperature in Celsius."""
    return float(_beta_interp(T_C))

def nu(T_C):
    """Kinematic viscosity as a function of temperature in Celsius."""
    return mu(T_C) / rho(T_C)
