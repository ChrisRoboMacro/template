import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import datetime

def create_economic_chart(x, y_datasets, chart_title, subtitle, y_label, labels=None, image_path='logo.jpg', line_widths=None):
    # Load the background image
    try:
        img = mpimg.imread(image_path)
    except FileNotFoundError:
        print("Error: Image file not found.")
        return

    fig, ax = plt.subplots()

    # Flatten all y values into a single array for percentile calculation and analysis
    all_y_values = np.concatenate(y_datasets)
    average_y = np.mean(all_y_values[:-13])  # Calculate mean of all but the most recent 13 data points
    max_y = np.max(all_y_values[:-13])      # Same for max

    # Calculate the 1st percentile for the lower bound
    lower_bound = np.percentile(all_y_values[:-13], 1)

    # Determine if the upper bound should be the 99th percentile or just the max value
    if max_y > 3 * average_y:
        upper_bound = np.percentile(all_y_values[:-13], 99)
    else:
        upper_bound = max_y

    # Ensure the most recent 13 data points are considered for bounds
    recent_y_values = all_y_values[-13:]
    if len(recent_y_values) > 0:
        y_min = min(lower_bound, np.min(recent_y_values))
        y_max = max(upper_bound, np.max(recent_y_values))
    else:
        y_min = lower_bound
        y_max = upper_bound

    # Determine the x and y bounds for setting the image background
    x_min, x_max = np.min(x), np.max(x)
    ax.imshow(img, aspect='auto', extent=[x_min, x_max, y_min, y_max], zorder=-1)

    # Define a custom darker pastel color palette
    darker_pastel_palette = sns.color_palette([
        (0.7, 0.5, 0.5),
        (0.5, 0.6, 0.7),
        (0.6, 0.7, 0.5),
        (0.7, 0.7, 0.5),
        (0.5, 0.5, 0.7),
        (0.7, 0.5, 0.7),
        (0.5, 0.7, 0.7),
        (0.7, 0.6, 0.5)
    ])

    # Validate or set default line widths
    if line_widths is None:
        line_widths = [2] * len(y_datasets)  # Default line width set to 2
    elif len(line_widths) != len(y_datasets):
        raise ValueError("line_widths list must be the same length as y_datasets")

    # Plot each dataset with limits applied and custom labels if provided
    if labels is None:
        labels = [f'Data Series {i+1}' for i in range(len(y_datasets))]
    for i, y in enumerate(y_datasets):
        sns.lineplot(x=x, y=np.clip(y, y_min, y_max), ax=ax, color=darker_pastel_palette[i % len(darker_pastel_palette)], linewidth=line_widths[i], label=labels[i])

    # Setting labels and titles
    if not np.issubdtype(type(x[0]), np.datetime64) and not isinstance(x[0], (datetime.date, datetime.datetime)):
        ax.set_xlabel('Time', fontsize=10, fontweight='bold', color='#888B8D')
    else:
        ax.set_xlabel('')  # Don't set any label if the x-axis represents dates or times.

    ax.set_ylabel(y_label, fontsize=10, fontweight='bold', color='#888B8D')

    plt.suptitle(chart_title, fontsize=14, fontweight='bold', color='#494B4D')
    plt.title(subtitle, fontsize=11, loc='left', fontstyle='italic', color='#888B8D')

    # Customizing the aesthetics
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.tick_params(axis='x', which='major', labelsize=10, width=2, colors='#888B8D')
    ax.tick_params(axis='y', which='major', labelsize=10, width=2, colors='#888B8D')

    # Create the legend with frame and specified face color
    legend = ax.legend(loc='best', frameon=True, facecolor='white', edgecolor='none')
    # Set the alpha after legend creation
    legend.get_frame().set_alpha(0.7)

    # Save and display the chart
    plt.savefig(f'{chart_title.lower().replace(" ", "_")}.png', dpi=300)
    plt.show()
