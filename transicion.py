import numpy as np
import matplotlib.pyplot as plt

# --- Configuración ---
dt = 0.1
T = 10.0
n = int(T / dt)
na = 300
a_vals = np.linspace(-1.5, 1.5, na)

# Parámetros
b_vals = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
w = 1.0
x0 = np.random.uniform(-1.0, 1.0) + 0j
dw_fijo = np.random.normal(0, np.sqrt(dt))
def f(a, x, w):
    return x * (a + 1j * w - np.abs(x)**2)

# --- Gráfica ---
plt.figure(figsize=(10, 7), dpi=100)

for b in b_vals:
    xf = np.zeros(na, dtype=complex)
    
    for j in range(na):
        x = x0
        # Generamos UN solo dw para toda la integración de este punto
         
        
        for i in range(n):
            # Usamos el mismo dw_fijo en cada iteración i
            x = x + (f(a_vals[j], x, w) * dt) + (b * x * dw_fijo)
        
        xf[j] = x

    # Graficar la línea para el valor actual de b
    plt.plot(a_vals, np.abs(xf), lw=1, label=f'b = {b}')

# --- Estética ---
plt.title('Simulación con ruido constante por trayectoria', fontsize=12)
plt.xlabel('Parámetro a', fontsize=10)
plt.ylabel('Amplitud $|x|$', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Valor de b", loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()