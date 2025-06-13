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

# Flow rate values (m^3/h) converted to velocity (m/s)
Q_vals = np.linspace(0.5, 6.0, 10) / 3600.0  # m^3/s
AREA = 1e-3  # 10 cm^2 in m^2
U_vals = Q_vals / AREA

# Temperature range in Celsius
T_vals = np.arange(300, 551, 25)

results = []
for T in T_vals:
    sigma = props.sigma(T)
    rho = props.rho(T)
    nu = props.nu(T)
    k = props.k(T)
    beta = props.beta(T)
    for U in U_vals:
        L_ha = mhd.characteristic_length_from_Ha_ratio(B, sigma, rho, U, HA2_OVER_RE)
        for q in q_values:
            L_gr = mhd.characteristic_length_from_Gr_ratio(B, sigma, rho, nu, G, beta, q, k, GR_OVER_HA2)
            L_re = L_ha  # derived from same ratio
            results.append({
                "T": T,
                "U": U,
                "q": q,
                "L_ha": L_ha,
                "L_gr": L_gr,
                "L_re": L_re,
            })

# Convert results to arrays for plotting (use first temperature as example)
T_example = T_vals[len(T_vals) // 2]
filtered = [r for r in results if r["T"] == T_example]
L_ha_grid = np.array([r["L_ha"] for r in filtered]).reshape(len(U_vals), len(q_values))
L_gr_grid = np.array([r["L_gr"] for r in filtered]).reshape(len(U_vals), len(q_values))
L_re_grid = np.array([r["L_re"] for r in filtered]).reshape(len(U_vals), len(q_values))
Q_grid = np.tile(q_values_MW, (len(U_vals), 1))
U_grid = np.tile(U_vals[:, None], (1, len(q_values)))

# Plotting
fig1, _ = plotting.plot_Lha_Lgr_q(L_ha_grid, L_gr_grid, Q_grid, title=f"T={T_example}C")
fig2, _ = plotting.plot_Lha_Lre_u(L_ha_grid, L_re_grid, U_grid, title=f"T={T_example}C")

# Mark contour where L_ha == L_gr
fig1.axes[0].contour(L_ha_grid, L_gr_grid, Q_grid, levels=[0], colors='r')

plt.show()
