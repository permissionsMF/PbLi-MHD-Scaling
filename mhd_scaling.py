import numpy as np

# Dimensionless numbers

def hartmann_number(B, L, sigma, rho, nu):
    """Hartmann number."""
    return B * L * np.sqrt(sigma / (rho * nu))


def reynolds_number(U, L, nu):
    """Reynolds number."""
    return U * L / nu


def grashof_number(g, beta, q, L, k, nu):
    """Grashof number based on surface heating."""
    return g * beta * q * L**4 / (k * nu**2)


# Characteristic length calculations

def characteristic_length_from_Ha_ratio(B, sigma, rho, U, ha2_over_re):
    """L from Ha^2/Re ratio."""
    return ha2_over_re * rho * U / (B**2 * sigma)


def characteristic_length_from_Gr_ratio(B, sigma, rho, nu, g, beta, q, k, gr_over_ha2):
    """L from Gr/Ha^2 ratio."""
    num = gr_over_ha2 * k * nu * B**2 * sigma
    den = g * beta * q * rho
    return np.sqrt(num / den)


def characteristic_length_from_Re_ratio(B, sigma, rho, nu, U, ha2_over_re):
    """L from Ha^2/Re ratio using the implied Reynolds number."""
    L_ha = characteristic_length_from_Ha_ratio(B, sigma, rho, U, ha2_over_re)
    ha = hartmann_number(B, L_ha, sigma, rho, nu)
    re = ha**2 / ha2_over_re
    return re * nu / U


# New inverse relationships -------------------------------------------------

def velocity_from_lengths(L_ha, L_re, B, sigma, rho, nu, ha2_over_re):
    """Flow velocity that satisfies ``Ha^2/Re`` for given lengths.

    Parameters
    ----------
    L_ha : ndarray or float
        Characteristic length derived from the Hartmann relation [m].
    L_re : ndarray or float
        Characteristic length associated with the Reynolds number [m].
    B : float
        Magnetic field strength in Tesla.
    sigma, rho, nu : float
        Material properties at the operating temperature.
    ha2_over_re : float
        Target ``Ha^2/Re`` interaction parameter.

    Returns
    -------
    ndarray or float
        Velocity ``U`` [m/s].
    """
    ha = hartmann_number(B, L_ha, sigma, rho, nu)
    re = ha**2 / ha2_over_re
    return re * nu / L_re


def heat_flux_from_length(L_gr, B, sigma, rho, nu, g, beta, k, gr_over_ha2):
    """Surface heat flux that satisfies ``Gr/Ha^2`` for a given ``L_Gr``.

    Parameters
    ----------
    L_gr : ndarray or float
        Characteristic length from the Grashof relation [m].
    B : float
        Magnetic field strength in Tesla.
    sigma, rho, nu, g, beta, k : float
        Material properties and gravitational acceleration.
    gr_over_ha2 : float
        Target ``Gr/Ha^2`` interaction parameter.

    Returns
    -------
    ndarray or float
        Heat flux ``q''`` [W/m^2].
    """
    num = gr_over_ha2 * k * nu * B**2 * sigma
    den = g * beta * rho * L_gr**2
    return num / den
