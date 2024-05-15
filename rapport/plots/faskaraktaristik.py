import matplotlib.pyplot as plt
import numpy as np

def arg_a(w):
    condition = np.logical_and(w <= 10, w >= 0)
    result = np.zeros_like(w)
    result[condition] = np.arctan((4*w[condition])/25) - np.arctan((16*w[condition])/(100-w[condition]**2))
    result[~condition] = np.arctan((4*w[~condition])/25) - (np.pi/2) - np.arctan((w[~condition]**2 - 100) / 16*w[~condition])
    return result

def arg_b(w):
    return (np.arctan(w/50) - 2*np.arctan(w/10))

def arg_c(w):
    return (np.arctan((13*w)/25) - np.arctan(w/2) - np.arctan(w/50))

t_values = np.linspace(0, 10000, 100000)
a_values = arg_a(t_values)
b_values = arg_b(t_values)
c_values = arg_c(t_values)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move both x and y axis to origin
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.xlim(0, 1000) 
plt.ylim(-2.5, 0)

# Set tick spacing in the axes
ax.xaxis.set_major_locator(plt.MultipleLocator(100))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

plt.plot(t_values, a_values , label="H_A(w)")
plt.plot(t_values, b_values , label="H_B(w)")
plt.plot(t_values, c_values , label="H_C(w)")

plt.title('systemfunktionernas faskaraktäristik')
plt.ylabel('arg(w)')
plt.xlabel('vinkelfrekvens (rad/s)')
plt.legend(loc="lower right")
plt.grid(True)
plt.savefig("plots/images/faskar.png")
plt.show()
