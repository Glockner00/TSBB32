import matplotlib.pyplot as plt
import numpy as np


def g_b(t):
    return (1 - np.exp(-10*t)- 8*t*np.exp(-10*t))

t_values = np.linspace(-10, 10, 1000)
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

plt.title('Amplitudskar.')
plt.ylabel('g(t)(m)')
plt.xlabel('Tid(s)')


plt.plot(t_values, b_values , label="g_b(t)")

plt.legend()
plt.grid(True)
plt.savefig("rapport/plots/images/stegsvar.png")
plt.show()
