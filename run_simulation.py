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
Q_max = 6.0 /3600 # m3/s

# Sweep ranges for characteristic lengths (in mm)
L_HA_MM = np.linspace(1.0, 100.0, 20)
L_GR_MM = np.linspace(1.0, 10.0, 20)
L_RE_MM = np.linspace(1.0, 100.0, 20)

q = np.linspace(0.0, 1E+06, 20) # W
U = np.linspace(0.0001, 0.005, 20) # m/s

def velocities_from_flowrate(Q_m3_per_h, L_array):
    """
    Compute array of flow velocities from volumetric flow rate and characteristic lengths,
    assuming square cross-section A = L^2.

    Parameters:
        Q_m3_per_h (float): Volumetric flow rate in m³/h
        L_array (np.ndarray): Array of characteristic lengths [m]

    Returns:
        np.ndarray: Array of flow velocities [m/s]
    """
    Q = Q_m3_per_h / 3600.0  # Convert to m³/s
    A_array = L_array ** 2   # Cross-sectional area [m²]
    U_array = Q / A_array    # Velocity [m/s]
    return U_array


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
    
    U_array = velocities_from_flowrate(6.0, L_re)
    U_array = np.linspace(0, 0.005, 20)
    
    Ha_array = mhd.hartmann_number(B, L_ha, sigma, rho, nu)
    Re_array = mhd.reynolds_number(U, L_re, nu)
    Gr_array = mhd.grashof_number(G, beta, q, L_gr, k, nu)
    
    
    results = []
    for Ha in Ha_array:
        row = []
        for heat_flux in q:
            
            Gr = GR_OVER_HA2 * Ha**2
            value = mhd.length_from_grashof(Gr, G, beta, heat_flux, k, nu)
            
            row.append(value)
        results.append(row)
        
    print(results)
    

    
    Ha_array = np.array(Ha_array)              # shape: (n,)
    q_array = np.array(q)                      # shape: (m,)
    Z = np.array(results)                      # shape: (n, m)
    
    # Create meshgrid for X and Y axes
    Q_mesh, Ha_mesh = np.meshgrid(q_array, Ha_array)  # shape: (n, m)
    
    # Create 3D surface plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(Q_mesh, Ha_mesh, Z, cmap='viridis', edgecolor='none')
    
    # Labels and title
    ax.set_xlabel("Heat Flux $q''$ [W/m²]")
    ax.set_ylabel("Hartmann Number (Ha)")
    ax.set_zlabel("Characteristic Length $L$ [m]")
    ax.set_title("Characteristic Length vs Heat Flux and Hartmann Number")
    
    # Colorbar
    fig.colorbar(surf, shrink=0.5, aspect=10)
    
    plt.tight_layout()
    plt.show()
      


    results2 = []
    for u in U_array:
        row = []
        for L in L_re:
            
            Re = mhd.reynolds_number(u, L, nu)
            value = (HA2_OVER_RE * Re)**0.5 
            
            row.append(value)
        results2.append(row)
        
    print(results2)




    # Assuming U_array, L_re, results2 are already defined
    U_array = np.array(U_array)        # shape (m,)
    L_array = np.array(L_re)           # shape (n,)
    Z = np.array(results2)             # shape (m, n)
    
    # Create meshgrid for plotting
    L_mesh, U_mesh = np.meshgrid(L_array, U_array)  # shape (m, n)
    
    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(L_mesh, U_mesh, Z, cmap='viridis', edgecolor='none')
    
    # Max Ha overlay
    Ha_max = B * L_array * np.sqrt(sigma / (rho * nu))
    U_line = np.full_like(L_array, U_array.max())
    ax.plot(L_array, U_line, Ha_max, color='red', linewidth=2.5, label='Max Ha (facility)')
    
    # Labels, legend, show
    ax.set_xlabel("Characteristic Length $L$ [m]")
    ax.set_ylabel("Flow Velocity $U$ [m/s]")
    ax.set_zlabel("Hartmann Number (Ha)")
    ax.set_title("Hartmann Number vs Flow Velocity and Length")
    ax.legend()
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.tight_layout()
    plt.show()

    """

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
    """


if __name__ == "__main__":
    main()
