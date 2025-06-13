import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused
import numpy as np


def plot_Lha_Lgr_q(L_ha, L_gr, q_values, title="L_Ha vs L_Gr vs heat flux"):
    """3D surface plot of L_Ha vs L_Gr vs heat flux."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    X, Y = np.meshgrid(L_ha, L_gr)
    Z = q_values

    surf = ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)
    ax.set_xlabel("L_Ha [m]")
    ax.set_ylabel("L_Gr [m]")
    ax.set_zlabel("q'' [MW/m^2]")
    ax.set_title(title)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    return fig, ax


def plot_Lha_Lre_u(L_ha, L_re, u_values, title="L_Ha vs L_Re vs velocity"):
    """3D surface plot of L_Ha vs L_Re vs velocity."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    X, Y = np.meshgrid(L_ha, L_re)
    Z = u_values

    surf = ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.8)
    ax.set_xlabel("L_Ha [m]")
    ax.set_ylabel("L_Re [m]")
    ax.set_zlabel("U [m/s]")
    ax.set_title(title)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    return fig, ax
