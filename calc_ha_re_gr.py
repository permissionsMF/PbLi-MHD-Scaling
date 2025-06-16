import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import product
from scipy.spatial import ConvexHull
from prop_correlations_Pb17atLi import *

# Input ranges
B_range = np.linspace(1, 4, 4)           # Tesla
L_range = np.linspace(0.005, 0.1, 10)    # meters
U_range = np.linspace(0.0001, 0.005, 10) # m/s
q_range = np.linspace(1e5, 1e6, 10)      # W/m^2
T_C_range = np.linspace(270, 550, 5)     # Celsius

G = 9.81  # m/s²

results = []
valid_temps = []

for T_C in T_C_range:
    T_K = T_C + 273.15
    try:
        # Check that temperature is within valid correlation ranges
        rho = density(T_K)
        nu = kinematicViscosity(T_K)
        beta = volumetricThermalExpansionCoeff(T_K)
        k = thermalConductivity(T_C) * 100  # W/cm.K to W/m.K
        sigma = electricalConductivity(T_K)
    except Exception as e:
        print(f"⛔ Skipping T_C = {T_C} °C due to: {e}")
        continue

    count_before = len(results)

    for B, L, U, q in product(B_range, L_range, U_range, q_range):
        Ha = B * L * np.sqrt(sigma / (rho * nu))
        Re = U * L / nu
        Gr = G * beta * q * L**4 / (k * nu**2)
        I_ha2_over_re = (Ha**2) / Re
        I_gr_over_ha2 = Gr / (Ha**2)
        I_gr_over_re2 = Gr / (Re**2)

        results.append([
            T_C, B, L, U, q, Ha, Re, Gr,
            I_ha2_over_re, I_gr_over_ha2, I_gr_over_re2
        ])

    count_after = len(results)
    print(f"✔ T_C = {T_C} °C — Data points added: {count_after - count_before}")
    valid_temps.append(T_C)

# Convert results to DataFrame
df = pd.DataFrame(results, columns=[
    "Temp_C", "B_T", "L_m", "U_mps", "q_Wm2",
    "Ha", "Re", "Gr", "I_ha2_over_re", "I_gr_over_ha2", "I_gr_over_re2"
])

# Log-log Convex Hull plot
df['log_Gr'] = np.log10(df['Gr'])
df['log_I'] = np.log10(df['I_ha2_over_re'])

points = df[['log_Gr', 'log_I']].dropna().values
hull = ConvexHull(points)

plt.figure(figsize=(10, 6))
plt.scatter(10**df['log_Gr'], 10**df['log_I'], alpha=0.3, c='#002D5A', label='Data Points')
for simplex in hull.simplices:
    plt.plot(10**points[simplex, 0], 10**points[simplex, 1], color='#C00000', lw=2)  # Red


plt.xscale('log')
plt.yscale('log')
plt.xlabel('Grashof Number (Gr)')
plt.ylabel('Ha² / Re')
plt.title('Experimental Capability Envelope: Ha²/Re vs Gr (Log-Log Scale)')
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# 🔍 Linear plot for the first valid temperature
if valid_temps:
    first_temp = valid_temps[0]
    df_first = df[df["Temp_C"] == first_temp]

    print(f"📌 Plotting data for T_C = {first_temp} °C — {len(df_first)} points")

    plt.figure(figsize=(10, 6))
    plt.scatter(df_first["Gr"], df_first["I_ha2_over_re"], c='green', alpha=0.6, label=f"{first_temp} °C")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Grashof Number (Gr)")
    plt.ylabel("Ha² / Re")
    plt.title(f"Ha² / Re vs Gr at {first_temp} °C (Linear Scale)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("⚠ No valid temperature data available for linear plot.")

# 📊 Range Summary
range_dict = {
    "Ha": (df["Ha"].min(), df["Ha"].max()),
    "Re": (df["Re"].min(), df["Re"].max()),
    "Gr": (df["Gr"].min(), df["Gr"].max()),
    "Ha^2 / Re": (df["I_ha2_over_re"].min(), df["I_ha2_over_re"].max()),
    "Gr / Ha^2": (df["I_gr_over_ha2"].min(), df["I_gr_over_ha2"].max()),
    "Gr / Re^2": (df["I_gr_over_re2"].min(), df["I_gr_over_re2"].max()),
}

print("\n📊 Experimental Capability Ranges:")
for key, (min_val, max_val) in range_dict.items():
    print(f" - {key:<12}: {min_val:.3e} to {max_val:.3e}")
