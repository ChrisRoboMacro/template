import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#github test

def create_economic_chart(x, y_datasets, chart_title, subtitle, y_label, image_path='logo.jpg'):
    # Load the background image
    try:
        img = mpimg.imread(image_path)
    except FileNotFoundError:
        print("Error: Image file not found.")
        return

    fig, ax = plt.subplots()

    # Determine the x and y bounds for setting the image background
    x_min, x_max = np.min(x), np.max(x)
    y_min, y_max = min(np.min(y) for y in y_datasets), max(np.max(y) for y in y_datasets)
    ax.imshow(img, aspect='auto', extent=[x_min, x_max, y_min, y_max], zorder=-1)

    # Define a custom darker pastel color palette
    darker_pastel_palette = sns.color_palette([
        (0.7, 0.5, 0.5),  # darker pastel red
        (0.5, 0.6, 0.7),  # darker pastel blue
        (0.6, 0.7, 0.5),  # darker pastel green
        (0.7, 0.7, 0.5),  # darker pastel yellow
        (0.5, 0.5, 0.7),  # darker pastel purple
        (0.7, 0.5, 0.7),  # darker pastel pink
        (0.5, 0.7, 0.7),  # darker pastel cyan
        (0.7, 0.6, 0.5)   # darker pastel orange
    ])

    # Plot each dataset
    for i, y in enumerate(y_datasets):
        sns.lineplot(x=x, y=y, ax=ax, color=darker_pastel_palette[i % len(darker_pastel_palette)], label=f'Data Series {i+1}')

    # Setting labels and titles
    if y_label.lower() != "time":  # Conditionally set the x-axis label, pointless if it just says "Time"
        ax.set_xlabel('Time', fontsize=12, fontweight='bold', color='#888B8D')
    ax.set_ylabel(y_label, fontsize=12, fontweight='bold', color='#888B8D')
    plt.suptitle(chart_title, fontsize=16, fontweight='bold', color='#494B4D')
    plt.title(subtitle, fontsize=12, loc='left', color='#888B8D')

    # Customizing the aesthetics
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.tick_params(axis='x', which='major', labelsize=10, width=2, colors='#888B8D')
    ax.tick_params(axis='y', which='major', labelsize=10, width=2, colors='#888B8D')
    
    # Legend positioning
    ax.legend(loc='best', frameon=False)  # Dynamically position the legend

    # Save and display the chart
    plt.savefig(f'{chart_title.lower().replace(" ", "_")}.png', dpi=300)
    plt.show()

# Example usage with multiple data series:
# x = np.linspace(0, 10, 100)
# y_datasets = [np.sin(x) * 10, np.cos(x) * 10, np.sin(x + np.pi / 3) * 10, np.sin(x - np.pi / 4) * 10]
# create_economic_chart(x, y_datasets, 'Multiple Data Chart', 'Various Sine Waves', 'Values')
