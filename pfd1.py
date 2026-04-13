import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#Parámetros
a = np.linspace(-10, 10, 99)
mu = np.linspace (0.1, 2.0, 10)

#Constante normalizada
def integral(r, a, mu):
    return r * np.exp((2 * a * r**2 - r**4) / (2 * mu**2))

#PFD
def Prob_polar(r, N, a, mu):
    exponente = (2 * a * r**2 - r**4) / (2 * mu**2)
    return N * r * np.exp(exponente)


#plt.figure(figsize=(10, 6))
r = np.linspace(0, np.sqrt(10)+1, 500)

colors = plt.cm.viridis(np.linspace(0, 1, len(a)))

for j, mu_val in enumerate (mu):
    if mu_val!=0:
        for i, a_val in enumerate(a):
            inv_N, _ = quad(integral, 0, np.inf, args=(a_val, mu_val))
            N = 1 / inv_N
            p_vals = Prob_polar(r, N, a_val, mu_val)
            plt.plot(r, p_vals, label=f'a = {a_val:.1f}, $\mu$ = {mu_val:.1f}', color=colors[i], lw=2)
#GRAFICA
    plt.title('Distribución de Probabilidad Polar $P(r)$ para distintos valores de $a$ y $\mu$' )
    plt.xlabel('Radio (r)')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True, linestyle='--', alpha=0.6)
    #plt.legend(title="Valor de parámetros")
    plt.show()