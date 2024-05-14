import matplotlib.pyplot as plt
import numpy as np

def H_A(w):
    return np.abs(np.sqrt(100**2 + (16*w)**2) / np.sqrt((100 - w**2)**2 + (16*w)**2))
def H_B(w):
    return np.abs(np.sqrt(100**2 + (2*w)**2) / (np.sqrt(100-w**2)**2 + (20*w)**2))
def H_C(w):
    return np.abs(np.sqrt(100**2 + (52*w)**2) / np.sqrt((100-w**2)**2 + (52*w)**2))

t_values = np.linspace(0, 2000, 10000)
a_values = H_A(t_values)
b_values = H_B(t_values)
c_values = H_C(t_values)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move both x and y axis to origin
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.xlim(0, 20) 
plt.ylim(0, 2)

# Set tick spacing in the axes
ax.xaxis.set_major_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))

plt.title('Amplitudskar.')
plt.ylabel('|H(w)|(m)')
plt.xlabel('vinkelfrekvens (rad/s)')


plt.plot(t_values, a_values, label="H_A(t)")
plt.plot(t_values, b_values, label="H_B(t)")
plt.plot(t_values, c_values, label="H_C(t)")
plt.legend()
plt.grid(True)
plt.savefig("images/amplitudskarliten.png")
plt.show()
