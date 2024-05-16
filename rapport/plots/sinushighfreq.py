import numpy as np
import matplotlib.pyplot as plt

# Definiera funktionerna
def x_1(t):
    return (np.sin(200 * t))  #Nedskalad 4000 gånger.

def y_1(t):
    return (np.sqrt(262769)/6409)*np.sin(200*t + np.arctan(25/512) - (np.pi/2))

# Skapa data
t = np.linspace(0, 1000, 300000)  # Skapa en array med tidspunkter
x = x_1(t)
y = y_1(t)

# Skapa diagram
plt.figure(figsize=(12, 8))
plt.plot(t, x, label="x_1(t)")
plt.plot(t, y, label="y_1(t)")
plt.xlim(0, 0.5)
plt.ylim(-1.5, 1.5)  
plt.xlabel('Tid (s)')
plt.legend()
plt.ylabel('N/m')
plt.title('Stationär sinusfinktion i högfrekvens')
plt.savefig("rapport/plots/images/sinhighfreq.png")
plt.grid(True)
plt.show()
