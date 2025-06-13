
---

### 🤖 `codex_instructions.md`

```markdown
# Codex Instructions

## Purpose

This repository is designed to use OpenAI Codex to automate the development of analytical tools for scaling mock-up designs using dimensionless MHD parameters.

## Input from User

Codex will be prompted using:
- DEMO-derived interaction parameters: `Ha²/Re` and `Gr/Ha²`
- Constraints from the test loop: magnetic field, flow rate, heat flux
- PbLi and SS316L material property models as functions of temperature

## Tasks for Codex

1. **Define Governing Equations**

   For dimensionless numbers:
   - Hartmann number:
     \[
     \text{Ha} = B L \sqrt{\frac{\sigma}{\rho \nu}}
     \]
   - Reynolds number:
     \[
     \text{Re} = \frac{U L}{\nu}
     \]
   - Grashof number (surface heating):
     \[
     \text{Gr} = \frac{g \beta q'' L^4}{k \nu^2}
     \]

2. **Rearrange equations to express \( L \) as a function of:**
   - Known interaction parameters: \( \text{Ha}^2/\text{Re} \), \( \text{Gr}/\text{Ha}^2 \)
   - Known variables: \( B, q'', U \)
   - Material properties: \( \rho(T), \nu(T), \sigma(T), k(T), \beta(T) \)

3. **Create functions to compute \( L(Ha) \), \( L(Re) \), and \( L(Gr) \)**  
   These should:
   - Use symbolic or numerical solvers to find \( L \)
   - Allow temperature as an input and use interpolated properties

4. **Plot the outputs:**
   - 3D surfaces:
     - \( L(Ha) \) vs \( L(Gr) \) vs \( q'' \)
     - \( L(Ha) \) vs \( L(Re) \) vs \( U \)
   - Highlight DEMO-equivalent values for reference

5. **Use Materials Data**
   - PbLi: density, dynamic viscosity, electrical conductivity, thermal conductivity, thermal expansion coefficient
   - SS316L: (as needed for comparison, optional)

## Output Format

Codex-generated modules should include:
- `mhd_scaling.py` — core logic
- `material_props.py` — interpolated material functions
- `plotting.py` — 3D visualisation
- `run_simulation.py` — parameter sweep and CLI

