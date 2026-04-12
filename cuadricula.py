import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

##PARAMETROS
dt = 0.001
T = 500.0
n = int(T/dt)
t = np.linspace(0, T, n)
S = 200  # 200 osciladores para una cuadrícula 10x20
K = 2.0  # acople
b = 0.4  # ruido

# Parámetros de los osciladores
# Mezclamos a < 0 y otros a > 0 
a = np.random.uniform(-1.0, 0.5, S) 
w = np.random.uniform(0.0, 5.0, S)
x0 = np.random.uniform(0, 2, S) * np.exp(1j * np.random.uniform(0, 2*np.pi, S))
x = np.zeros((n, S), dtype=complex)

#Función de dinámica 
def f(a, x, w, K, acople):
    # Ecuación: x*(a + iw - |x|^2) + K*(promedio - x)
    return x * (a + 1j*w - np.abs(x)**2) + K * (acople - x)

#Euler-Maruyama
x[0, :] = x0
for i in range(1, n):
    #DUDA; si no defino el ruido aqui sale raro
    dw = (np.random.normal(0, np.sqrt(dt), S) + 1j * np.random.normal(0, np.sqrt(dt), S))
    
    # Campo medio (promedio de las posiciones de todos los osciladores)
    acople_medio = np.mean(x[i-1, :])
    
    # Evolución temporal
    drift = f(a, x[i-1, :], w, K, acople_medio)
    difusion = b * x[i-1, :] * dw
    x[i, :] = x[i-1, :] + (drift * dt) + difusion



#Calculo de estadísticos finales 
estados_finales = x[-1, :]
amplitudes_finales = np.abs(estados_finales)
fases_finales = np.angle(estados_finales)
amp_max = np.max(amplitudes_finales) if np.max(amplitudes_finales) > 0 else 1.0


##GRAFICAS

#Cuadrícula 10x20 (Rojo a Verde)
amplitudes_grid = amplitudes_finales.reshape((10, 20)) #convierto los datos a matriz
colors = [(1, 0, 0), (1, 1, 0), (0, 0.8, 0)] #defino el gradiente de color
n_bins = 100 #profundidad del degradado
cmap_name = 'rojo_verde'
cm_rv = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)#crea el mapa de colores
plt.figure(figsize=(7, 6))
im = plt.imshow(amplitudes_grid, cmap=cm_rv, vmin=0, vmax=amp_max, origin='lower') #definicion de la asignacion de colores segun amplitudes
plt.title('Cuadrícula 10x10: Amplitudes de los Osciladores')
plt.xlabel('Columna')
plt.ylabel('Fila')
cbar = plt.colorbar(im) #Dibuja la barra de colores al lado del gráfico
cbar.set_label('Amplitud $|x|$')
cbar.set_ticks([0, amp_max/2, amp_max])
cbar.set_ticklabels(['0 (Mín/Rojo)', 'Medio (Amarillo)', f'{amp_max:.2f} (Máx/Verde)'])

# Representación en la Circunferencia Plano Complejo
plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar') #grafica en polares
sc = ax.scatter(fases_finales, amplitudes_finales, c=amplitudes_finales, cmap=cm_rv, edgecolors='k', alpha=0.8)#aplicamos el mismo mapa de colores de antes
ax.set_theta_zero_location('E') # El cero a la derecha
ax.set_title(r'Estados Finales en el Plano Complejo ($r e^{i\theta}$)', pad=20)
ax.set_ylim(0, amp_max * 1.1)

#Gráficas 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
sl = np.arange(S)
ax1.scatter(sl, amplitudes_finales, color='green', alpha=0.6)
ax1.set_title('Amplitudes Finales')
ax1.set_ylabel(r'Amplitud $|x_j|$')
ax1.grid(True, linestyle='--')
ax2.scatter(sl, fases_finales, color='blue', alpha=0.6)
ax2.set_title('Fases Finales')
ax2.set_ylabel(r'Fase $\arg(x_j)$ (rad)')
ax2.set_ylim(-np.pi, np.pi)
ax2.grid(True, linestyle='--')

plt.tight_layout()
plt.show()