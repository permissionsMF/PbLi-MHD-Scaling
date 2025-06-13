import numpy as np
import matplotlib.pyplot as plt

import material_props as props
import mhd_scaling as mhd
import plotting

# Target dimensionless interaction parameters from DEMO
HA2_OVER_RE = 8.22e5
GR_OVER_HA2 = 0.624

B = 4.0  # Tesla
G = 9.81  # m/s^2

# Heat flux values (MW/m^2 -> W/m^2)
q_values_MW = np.linspace(0.1, 1.0, 10)
q_values = q_values_MW * 1e6

# Flow velocity range (m/s)
U_vals = np.logspace(np.log10(1e-4), np.log10(5e-3), 20)

# Temperature range in Celsius
T_vals = np.arange(300, 551, 25)

for T in T_vals:
    sigma = props.sigma(T)
    rho = props.rho(T)
    nu = props.nu(T)
    k = props.k(T)
    beta = props.beta(T)

    L_ha_grid = np.zeros((len(U_vals), len(q_values)))
    L_gr_grid = np.zeros_like(L_ha_grid)

    for i, U in enumerate(U_vals):
        L_ha = mhd.characteristic_length_from_Ha_ratio(
            B, sigma, rho, U, HA2_OVER_RE
        )
        for j, q in enumerate(q_values):
            L_gr = mhd.characteristic_length_from_Gr_ratio(
                B, sigma, rho, nu, G, beta, q, k, GR_OVER_HA2
            )
            L_ha_grid[i, j] = L_ha
            L_gr_grid[i, j] = L_gr

    L_diff = L_ha_grid - L_gr_grid
    L_avg = 0.5 * (L_ha_grid + L_gr_grid)

    U_grid, q_grid = np.meshgrid(U_vals, q_values_MW, indexing="ij")
    fig, _ = plotting.plot_length_match(
        U_grid, q_grid, L_avg, L_diff, title=f"T={T}C"
    )
    fig.savefig(f"length_match_{T}C.png")

plt.show()
