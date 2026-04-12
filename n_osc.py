#N OSCILADORES, devuelve grafica de puntos con la distribucion de amplitudes y fases finales

import numpy as np
import matplotlib.pyplot as plt


#tiempo
dt=0.001
T=200.0
n=int(T/dt)
t=np.linspace(0,T,n)
S=100
K=2.0

#matriz posicion
#x=np.zeros((n,S), dtype=complex)


#parametros
b=0.1 #ruido
x=np.zeros((n,S), dtype=complex)
a=np.random.uniform(-1.5, 0.5, S) #distribución de los parametros de bifurcacion
w=np.random.uniform(0.0,5.0, S) #distribucion de las frecuencias naturales de los osciladores
x0=np.random.uniform(low=0.0, high=10.0, size=S) #generación aleatoria de las condiciones inciales
#funcion de drift y difusion
def f(a, x, w, K, acople, S):
    return x*(a + 1j*w - np.abs(x)**2) + K * (acople/S-x)

#iteracciones
x[0,:] = x0
for i in range(1,n):
    dw = np.random.normal(0, np.sqrt(dt))
    acople=0.0
    acople=np.sum(x[i-1,:]) #generacion del termino cruzado del modelo
    for j in range (S):
        x[i,j] = x[i-1,j] + (f(a[j],x[i-1,j],w[j],K, acople,S)* dt) + (b * x[i-1,j] * dw)


#Calculo de estadísticos finales e impresión en terminal
media_amplitud = np.mean(np.abs(x[n-1,:]))
media_fase= np.mean(np.angle(x[n-1,:]))
desviacion_amplitud= np.std(np.abs(x[n-1,:]))
desviacion_fase= np.std(np.angle(x[n-1,:]))
print("Media de amplitud:", media_amplitud)
print("Media de fase:", media_fase)
print("Desviación estándar de amplitud:", desviacion_amplitud)
print("Desviación estándar de fase:", desviacion_fase)

sl=np.linspace(0,S-1,S)
#Grafica de amplitudes finales
plt.figure(figsize=(8,8),dpi=100)
plt.scatter(sl, np.abs(x[n-1,:]),lw=0.6, color='#1f77b4', alpha=0.7, label=' Amplitudes finales')
plt.title('Amplitudes finales de los osciladores' , fontsize=10)
plt.xlabel('Índice del oscilador', fontsize=10)
plt.ylabel('Amplitud', fontsize=10)
plt.axhline(0, color='black', lw=1) # Línea base
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small') # Leyenda fuera
plt.tight_layout()
plt.show()

#Grafica de fases finales
plt.figure(figsize=(8,8),dpi=100)
plt.scatter(sl, np.angle(x[n-1,:]),lw=0.6, color='#1f77b4', alpha=0.7, label=' Amplitudes finales')
plt.title('Fases finales de los osciladores' , fontsize=10)
plt.xlabel('Índice del oscilador', fontsize=10)
plt.ylabel('Fase', fontsize=10)
plt.axhline(0, color='black', lw=1) # Línea base
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small') # Leyenda fuera
plt.tight_layout()
plt.show()

#¿Puedo hacerlo en la circunferencia de complejos?
