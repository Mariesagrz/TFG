import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

#Parámetros
dt = 0.01  
T = 100.0   
n = int(T/dt)
t = np.linspace(0, T, n)

b = [0.0, 0.1, 0.3, 0.6] 
a, w = -1.0, 1.0
x0 = np.random.normal(-0.5, 0.5) + 1j * np.random.normal(0.0, 0.0)

cmap = get_cmap('viridis')
colores = [cmap(i) for i in np.linspace(0, 0.9, len(b))]

resultados = []
for b_j in b:
    x = np.zeros(n, dtype=complex)
    x[0] = x0
    for i in range(1, n):
        dw = (np.random.normal(0, np.sqrt(dt)) + 1j * np.random.normal(0, np.sqrt(dt)))
        drift = x[i-1] * (a + 1j*w - np.abs(x[i-1])**2) * dt
        difusion = b_j * x[i-1] * dw
        x[i] = x[i-1] + drift + difusion
    
    
    fase= np.angle(x) % (2 * np.pi)
    
    resultados.append({'b': b_j, 'x': x, 'amp': np.abs(x), 'fase': fase})


#PLANO DE FASE
plt.figure(figsize=(7, 7))
for i, res in enumerate(resultados):
    plt.plot(res['x'].real, res['x'].imag, color=colores[i], lw=0.7, label=f'b={res["b"]}')
plt.title('Plano de Fase')
plt.legend()
plt.grid(True, alpha=0.3)

#AMPLITUD
plt.figure(figsize=(10, 4))
for i, res in enumerate(resultados):
    plt.plot(t, res['amp'], color=colores[i], lw=1.2, label=f'b={res["b"]}')
plt.title('Amplitud')
plt.legend()
plt.grid(True, alpha=0.3)

#FASE (0 a 2pi)
plt.figure(figsize=(10, 4))
for i, res in enumerate(resultados):
    plt.plot(t, res['fase'], color=colores[i], lw=1.2, label=f'b={res["b"]}')
plt.title('Evolución de la Fase (Rango $[0, 2\pi)$)')
plt.ylabel('Fase (rad)')
plt.xlabel('Tiempo')
plt.yticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], 
           ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.ylim(-0.1, 2*np.pi + 0.1)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

plt.show()