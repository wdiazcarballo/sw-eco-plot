import matplotlib.pyplot as plt
import numpy as np

# Data: Year and Team Size with Company Colors
data = {
    "WhatsApp": {
        "years": [2009, 2014],
        "sizes": [2, 55],
        "color": "#25D366",  # WhatsApp green
    },
    "Instagram": {
        "years": [2010, 2012],
        "sizes": [2, 13],
        "color": "#E4405F",  # Instagram pink
    },
    "Facebook": {
        "years": [2004, 2012],
        "sizes": [5, 5000],
        "color": "#1877F2",  # Facebook blue
    },
    "Google Maps": {
        "years": [2004, 2020],
        "sizes": [50, 1500],
        "color": "#4285F4",  # Google Maps blue
    },
    "Microsoft Office": {
        "years": [1989, 2020],
        "sizes": [50, 3000],
        "color": "#F25022",  # Microsoft Office orange
    },
    "Fortnite": {
        "years": [2011, 2020],
        "sizes": [50, 700],
        "color": "#7A42F4",  # Fortnite purple
    },
    "Windows 10": {
        "years": [2014, 2020],
        "sizes": [2000, 5000],
        "color": "#00A4EF",  # Windows blue
    },
}

# Plotting the data
plt.figure(figsize=(14, 10))

for product, values in data.items():
    years = values["years"]
    sizes = values["sizes"]
    color = values["color"]
    plt.plot(years, sizes, marker='o', color=color, label=product, linewidth=2, markersize=8)
    
    # Add labels for each data point
    for year, size in zip(years, sizes):
        plt.text(year, size, f'{size}', fontsize=10, ha='right' if year == years[0] else 'left', color=color)

# Add titles and labels
plt.title("Growth of Development Teams Over Time for Different Software Products", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Team Size", fontsize=14)
plt.xticks(np.arange(1989, 2021, step=2))
plt.grid(True, which="both", linestyle='--', linewidth=0.5)

# Add legend
plt.legend()

# Show the plot
plt.show()
