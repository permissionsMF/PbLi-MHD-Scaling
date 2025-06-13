import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused
import numpy as np


def plot_Lha_Lgr_q(L_ha, L_gr, q_values, title="L_Ha vs L_Gr vs heat flux"):
    """3D surface plot of L_Ha vs L_Gr vs heat flux.

    The function accepts either 1D vectors for ``L_ha`` and ``L_gr`` or full 2D
    grids. When vectors are provided a mesh grid is created internally.  If the
    inputs are already 2D and share the same shape as ``q_values`` they are used
    directly.  This prevents broadcasting errors when the caller has already
    generated the grids.
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    if L_ha.ndim == 1 and L_gr.ndim == 1:
        X, Y = np.meshgrid(L_ha, L_gr)
    else:
        # assume arrays are already shaped correctly
        X, Y = L_ha, L_gr

    Z = q_values

    surf = ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)
    ax.set_xlabel("L_Ha [m]")
    ax.set_ylabel("L_Gr [m]")
    ax.set_zlabel("q'' [MW/m^2]")
    ax.set_title(title)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    return fig, ax


def plot_Lha_Lre_u(L_ha, L_re, u_values, title="L_Ha vs L_Re vs velocity"):
    """3D surface plot of L_Ha vs L_Re vs velocity.

    Similar to :func:`plot_Lha_Lgr_q`, this helper accepts either vector inputs
    or precomputed grids to provide greater flexibility.
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    if L_ha.ndim == 1 and L_re.ndim == 1:
        X, Y = np.meshgrid(L_ha, L_re)
    else:
        X, Y = L_ha, L_re

    Z = u_values

    surf = ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.8)
    ax.set_xlabel("L_Ha [m]")
    ax.set_ylabel("L_Re [m]")
    ax.set_zlabel("U [m/s]")
    ax.set_title(title)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    return fig, ax

def plot_length_match(U, q, L, diff, threshold=1e-3, title="Characteristic length match"):
    """Contour plot of characteristic length with match indication.

    Parameters
    ----------
    U : ndarray
        2D grid of flow velocity values in m/s.
    q : ndarray
        2D grid of surface heat flux values in MW/m^2.
    L : ndarray
        2D grid of averaged characteristic lengths [m].
    diff : ndarray
        2D grid of ``L_Ha - L_Gr`` differences.
    threshold : float, optional
        Contour level used to highlight where ``|L_Ha - L_Gr|`` is small.
    title : str, optional
        Plot title.
    """
    fig, ax = plt.subplots()
    cf = ax.contourf(U, q, L, cmap="viridis")
    cbar = fig.colorbar(cf, ax=ax)
    cbar.set_label("L [m]")
    ax.contour(U, q, np.abs(diff), levels=[threshold], colors="r")
    ax.set_xlabel("U [m/s]")
    ax.set_ylabel("q'' [MW/m^2]")
    ax.set_title(title)
    return fig, ax
