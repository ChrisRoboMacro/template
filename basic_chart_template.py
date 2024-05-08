import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load your image
img = mpimg.imread('logo.jpg')

# Create a figure and axes
fig, ax = plt.subplots()

# Generate some example data
x = np.linspace(-10, 10, 100)  # Example data includes negative values
y1 = np.sin(x) * 10  # Scale sine wave for better visualization
y2 = np.cos(x) * 10  # Second data set
y3 = np.sin(x + np.pi / 3) * 10  # Third data set, phase shifted sine wave

# Determine the range of x and y to set image extent dynamically
x_min, x_max = x.min(), x.max()
y_min, y_max = min(y1.min(), y2.min(), y3.min()), max(y1.max(), y2.max(), y3.max())

# Set the image as the background
ax.imshow(img, aspect='auto', extent=[x_min, x_max, y_min, y_max], zorder=-1)

# Define a custom darker pastel color palette
darker_pastel_palette = sns.color_palette([
    (0.8, 0.6, 0.6),  # darker pastel red
    (0.6, 0.7, 0.8),  # darker pastel blue
    (0.7, 0.8, 0.6),  # darker pastel green
])

# Create seaborn line plots using the custom darker pastel palette
sns.lineplot(x=x, y=y1, ax=ax, color=darker_pastel_palette[0], label='Sine Wave')
sns.lineplot(x=x, y=y2, ax=ax, color=darker_pastel_palette[1], label='Cosine Wave')
sns.lineplot(x=x, y=y3, ax=ax, color=darker_pastel_palette[2], label='Shifted Sine Wave')

# Conditionally set labels for the axes
x_label = "Time"
if x_label.lower() != "time":  # Only set the xlabel if it's not "Time"
    ax.set_xlabel(x_label, fontsize=12, fontweight='bold', color='#888B8D')
ax.set_ylabel('Value', fontsize=12, fontweight='bold', color='#888B8D')

# Set title and subtitle with specific hex colors
title = "Main Title: Time Series Analysis"
subtitle = "Sub Title: Sine, Cosine, and Shifted Sine Waves"
plt.suptitle(title, fontsize=16, fontweight='bold', color='#494B4D')
plt.title(subtitle, fontsize=12, loc='left', color='#888B8D')

# Customize the axes
ax.spines['top'].set_visible(False)  # Hide the top border
ax.spines['right'].set_visible(False)  # Hide the right border
ax.spines['left'].set_linewidth(2)  # Make left border thicker
ax.spines['bottom'].set_linewidth(2)  # Make bottom border thicker

# Customize ticks
ax.tick_params(axis='x', which='major', labelsize=10, width=2, colors='#888B8D')
ax.tick_params(axis='y', which='major', labelsize=10, width=2, colors='#888B8D')

# Add a legend (key) dynamically positioned
legend = ax.legend(loc='best', frameon=False)  # Position legend dynamically to avoid covering data
# Set legend text color
plt.setp(legend.get_texts(), color='#524F4B')

# Save the figure
plt.savefig('seaborn_chart_with_background_and_three_lines_darker_pastels.png', dpi=300)

# Display the plot
plt.show()
