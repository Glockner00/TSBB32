import matplotlib.pyplot as plt
import numpy as np

def h_A(t):
    return (16*np.exp(-8*t)*np.cos(6*t) - (14/3)*np.exp(-8*t)*np.sin(6*t))

def h_B(t):
    return (2*np.exp(-10*t) + 80*t*np.exp(-10*t))

def h_C(t):
    return ((625/12) * np.exp(-50*t) - (1/12)*np.exp(-2*t))

t_values = np.linspace(-10, 10, 10000)
a_values = h_A(t_values)
b_values = h_B(t_values)
c_values = h_C(t_values)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move both x and y axis to origin
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.xlim(-1, 1)
plt.ylim(-10, 55)

# Set tick spacing in the axes
ax.xaxis.set_major_locator(plt.MultipleLocator(0.3))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))

plt.title('Impulssvar')
plt.xlabel('Tid(s)')
plt.ylabel('h(t)(m)')


plt.plot(t_values, a_values, label="h_A(t)")
plt.plot(t_values, b_values, label="h_B(t)")
plt.plot(t_values, c_values, label="h_C(t)")
plt.legend()
plt.grid(True)
plt.savefig("images/impulssvar.png")
plt.show()
