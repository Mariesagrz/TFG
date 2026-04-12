import numpy as np
import matplotlib.pyplot as plt


#tiempo
dt=0.001
T=10.0
n=int(T/dt)
t=np.linspace(0,T,n)

#vector posicion
x=np.zeros(n, dtype=complex)


#parametros
b=0.4
a=10.0
w=1.0
x0=np.random.uniform(low=0.0, high=10.0)


#funcion de drift y difusion
def f(a, x, w):
    return x*(a + 1j*w - np.abs(x)**2)



#iteracciones
x[0] = x0
for i in range(1, n):
    dw = np.random.normal(0, np.sqrt(dt))
    x[i] = x[i-1] + (f(a,x[i-1],w)* dt) + (b * x[i-1] * dw)


tr=np.zeros((n-50))
xr=np.zeros((n-50),dtype=complex)
for i in range(50,n):
    tr[i-50]=t[i]
    xr[i-50]=x[i]

#Grafica en complejos
plt.figure(figsize=(8, 8), dpi=100)
plt.plot(xr.real, xr.imag, lw=0.6, color='#1f77b4', alpha=0.7, label='Trayectoria SDE')
plt.title('Simulación de Euler-Maruyama, plano de fase', fontsize=10)
plt.xlabel('Real', fontsize=10)
plt.ylabel('Imaginaria', fontsize=10)
plt.axhline(0, color='black', lw=1) # Línea base
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small') # Leyenda fuera
plt.tight_layout()
plt.show()

amplitud = np.abs(xr)
fase = np.angle(xr)

#Grafico amplitu y fase

plt.figure(figsize=(10, 4))
plt.plot(tr, amplitud, color='crimson', lw=1.2)
plt.axhline(np.sqrt(a), color='black', ls='--', label='$\sqrt{a}$ (Teórico)')
plt.title('Evolución de la Amplitud en el Tiempo', fontsize=12)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud $|z|$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(tr, fase, color='forestgreen', lw=1.2)
plt.title('Evolución de la Fase (Unwrapped)', fontsize=12)
plt.xlabel('Tiempo')
plt.ylabel('Fase (rad)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
#¿se supone que x es un numero complejo?
#habria que representar solo a partir de un valor
#comprobar que la media de los valores a partir de ese tiempo esta en el radio que buscamos