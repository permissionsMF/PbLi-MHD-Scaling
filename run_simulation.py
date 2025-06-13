import numpy as np
import matplotlib.pyplot as plt

import material_props as props
import mhd_scaling as mhd
import plotting

# Target DEMO interaction parameters
HA2_OVER_RE = 8.22e5
GR_OVER_HA2 = 0.624

B = 4.0  # Tesla (constant)
G = 9.81  # m/s^2

# Heat fluxes and velocities
q_values_MW = np.linspace(0.1, 1.0, 10)
q_values = q_values_MW * 1e6
U_vals = np.logspace(np.log10(1e-4), np.log10(5e-3), 20)


def main() -> None:
    """Generate L(Ha)-L(Re)-U and L(Ha)-L(Gr)-q'' plots at 330°C."""

    T = 330  # Celsius
    sigma = props.sigma(T)
    rho = props.rho(T)
    nu = props.nu(T)
    k = props.k(T)
    beta = props.beta(T)

    # Characteristic lengths for each velocity and heat flux
    L_ha_vals = np.array(
        [mhd.characteristic_length_from_Ha_ratio(B, sigma, rho, U, HA2_OVER_RE) for U in U_vals]
    )
    L_re_vals = np.array(
        [mhd.characteristic_length_from_Re_ratio(B, sigma, rho, nu, U, HA2_OVER_RE) for U in U_vals]
    )
    L_gr_vals = np.array(
        [mhd.characteristic_length_from_Gr_ratio(B, sigma, rho, nu, G, beta, q, k, GR_OVER_HA2) for q in q_values]
    )

    # Convert to millimetres for plotting convenience
    L_ha_mm = 1e3 * L_ha_vals
    L_re_mm = 1e3 * L_re_vals
    L_gr_mm = 1e3 * L_gr_vals

    # Build grids for plotting helpers
    q_grid = np.tile(q_values_MW[:, None], (1, len(L_ha_mm)))
    u_grid = np.tile(U_vals[:, None], (1, len(L_ha_mm)))

    fig1, _ = plotting.plot_Lha_Lgr_q(
        L_ha_mm,
        L_gr_mm,
        q_grid,
        title="L_Ha vs L_Gr vs heat flux (T=330C)",
    )
    fig1.savefig("Lha_Lgr_heatflux.png")

    fig2, _ = plotting.plot_Lha_Lre_u(
        L_ha_mm,
        L_re_mm,
        u_grid,
        title="L_Ha vs L_Re vs velocity (T=330C)",
    )
    fig2.savefig("Lha_Lre_velocity.png")

    plt.show()


if __name__ == "__main__":
    main()
