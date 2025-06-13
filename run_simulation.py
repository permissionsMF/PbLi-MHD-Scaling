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

# Sweep ranges for characteristic lengths (in mm)
L_HA_MM = np.linspace(1.0, 10.0, 20)
L_GR_MM = np.linspace(1.0, 10.0, 20)
L_RE_MM = np.linspace(1.0, 10.0, 20)


def main() -> None:
    """Generate L(Ha)-L(Re)-U and L(Ha)-L(Gr)-q'' plots at 330°C."""

    T = 330  # Celsius
    sigma = props.sigma(T)
    rho = props.rho(T)
    nu = props.nu(T)
    k = props.k(T)
    beta = props.beta(T)

    L_ha = L_HA_MM / 1e3
    L_gr = L_GR_MM / 1e3
    L_re = L_RE_MM / 1e3

    L_ha_mm = L_HA_MM
    L_gr_mm = L_GR_MM
    L_re_mm = L_RE_MM

    # Compute q'' and U for each length combination
    LHA_grid, LGR_grid = np.meshgrid(L_ha, L_gr, indexing="xy")
    q_grid = mhd.heat_flux_from_length(
        LGR_grid, B, sigma, rho, nu, G, beta, k, GR_OVER_HA2
    ) / 1e6  # convert to MW/m^2

    LHA_grid_U, LRE_grid_U = np.meshgrid(L_ha, L_re, indexing="xy")
    u_grid = mhd.velocity_from_lengths(
        LHA_grid_U, LRE_grid_U, B, sigma, rho, nu, HA2_OVER_RE
    )

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
