#PFD CORREGIDA PARA UN SOLO OSCILADOR Y NORMALIZADA

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1. Parámetros
a = 1.0
mu = 1.0

# 2. Función para la integral de normalización (N^-1)
def integrand(r, a, mu):
    # Esta es la parte r * exp(...) de tu imagen
    return r * np.exp((2 * a * r**2 - r**4) / (2 * mu**2))

# Calculamos N
inv_N, _ = quad(integrand, 0, np.inf, args=(a, mu))
N = 1 / inv_N

# 3. Definición de la PDF marginal de r: P(r) = N * r * exp(...)
def P_radial(r, N, a, mu):
    exponent = (2 * a * r**2 - r**4) / (2 * mu**2)
    return N * r * np.exp(exponent)

# 4. Generar datos para la gráfica
r_vals = np.linspace(0, 3, 500)
p_vals = P_radial(r_vals, N, a, mu)

# 5. Gráfico 2D
plt.figure(figsize=(9, 5))
plt.plot(r_vals, p_vals, label=f'a={a}, $\mu$={mu}', color='royalblue', lw=2)
plt.fill_between(r_vals, p_vals, alpha=0.2, color='royalblue')

plt.title('Distribución de Probabilidad Radial $P(r)$')
plt.xlabel('Radio (r)')
plt.ylabel('Densidad de Probabilidad')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()