# PbLi-MHD-Scaling

This repository supports the design of MHD mock-ups for PbLi flow testing, aiming to match key dimensionless parameters (Hartmann, Reynolds, and Grashof numbers) relevant to DEMO reactor blanket regions.

We use dimensionless interaction parameters from the DEMO reference design:
- **Ha² / Re = 8.22×10⁵**
- **Gr / Ha² = 6.24×10⁻¹**

## Objective

- Calculate the characteristic length scales \( L \) for MHD similarity under constrained test conditions:
- Magnetic field \( B = 4 \, \text{T} \)
- Surface heat flux \( q'' = 0.1 \rightarrow 1.0 \, \text{MW/m²} \)
- Flow velocity ( U = 1e-4 -> 5e-3 m/s )
  - Constant operating temperature of **330°C**
- Temperature-dependent material properties for:
  - PbLi alloy (density, viscosity, conductivity, thermal conductivity, expansion coefficient)
  - SS316L structure (used for comparison)

## Features

- Derive characteristic lengths \( L(Ha) \), \( L(Re) \), and \( L(Gr) \)
- Explore interaction parameters:
  - \( \frac{\text{Ha}^2}{\text{Re}} \)
  - \( \frac{\text{Gr}}{\text{Ha}^2} \)
  - \( \frac{\text{Gr}}{\text{Re}^2} \)
- Generate 3D plots:
  - \( L(Ha) \) vs \( L(Re) \) vs flow velocity \( U \)
  - \( L(Ha) \) vs \( L(Gr) \) vs heat flux \( q'' \)
  - Sweep ``L`` values directly to compute the required
    heat flux or velocity for the target interaction parameters

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
python run_simulation.py
