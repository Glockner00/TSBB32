import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x_data = [-10]
y_data = [0]

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Set axes limits
plt.xlim(-30, 30)
plt.ylim(-30, 30)

# Set tick spacing in the axes
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))

# Fill area to the right of x = XX with transparent blue
fill_area = mpatches.Rectangle(
    xy=(-10, -30),  # The bottom left corner coordinates of the rectangle
    width=40,       # The widht of the rectangle
    height=60,      # The height of the rectangle
    color='blue',   # Fill color
    alpha=0.2,      # Transparancy
    zorder=-1       # Ensures the shaded area is drawn behind the plot elements.
)
ax.add_patch(fill_area)

# Plot markers
scatter = plt.scatter(x_data, y_data, color='red', marker='x')

# Legend labels with coordinates
labels = [f'polnollställe ({x}, j{y})' for x, y in zip(x_data, y_data)]

# Create legend
legend_handles = [mpatches.Patch(color='red', label=labels[0])]
legend_handles.append(mpatches.Patch(color='blue', alpha=0.2, label='konvergensområde: Re(s)>-10'))

plt.legend(handles=legend_handles, loc='upper right')

plt.title('H_B(s)')
plt.xlabel('Im(s)')
plt.ylabel('Re(s)')

ax.xaxis.set_label_position("top")
ax.yaxis.set_label_position("right")

plt.grid(True)

# Save plot
plt.savefig('images/H_B(s).png')
plt.show()