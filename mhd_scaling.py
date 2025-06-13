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
