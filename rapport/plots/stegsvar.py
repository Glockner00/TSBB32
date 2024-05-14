import matplotlib.pyplot as plt
import numpy as np

def g_a(t):
    term1 = (32 - 32*np.exp(-8*t) * np.cos(6*t) + 24*np.exp(-8*t) *np.sin(6*t))/25
    term2 = -((21*np.exp(8*t) - 28*np.sin(6*t) - 21*np.cos(6*t))/(75*np.exp(8*t)))
    return (term1 + term2)

def g_b(t):
    return (1 - np.exp(-10*t) - 8*t*np.exp(-10*t))

def g_c(t):
    pass

t_values = np.linspace(-10, 10, 1000)
a_values = g_a(t_values)
b_values = g_b(t_values)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move both x and y axis to origin
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.xlim(0, 1) 
plt.ylim(0, 2)

# Set tick spacing in the axes
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))

plt.plot(t_values, a_values , label="g_a(t)")
plt.plot(t_values, b_values , label="g_b(t)")

plt.title('Stegsvar')
plt.ylabel('g(t)(m)')
plt.xlabel('Tid(s)')
plt.legend()
plt.grid(True)

plt.savefig("rapport/plots/images/stegsvar.png")

plt.show()
