import matplotlib.pyplot as plt
import numpy as np

# Data: Year and Team Size
data = {
    "WhatsApp": {
        "years": [2009, 2014],
        "sizes": [2, 55],
    },
    "Instagram": {
        "years": [2010, 2012],
        "sizes": [2, 13],
    },
    "Facebook": {
        "years": [2004, 2012],
        "sizes": [5, 5000],
    },
    "Google Maps": {
        "years": [2004, 2020],
        "sizes": [50, 1500],
    },
    "Microsoft Office": {
        "years": [1989, 2020],
        "sizes": [50, 3000],
    },
    "Fortnite": {
        "years": [2011, 2020],
        "sizes": [50, 700],
    },
    "Windows 10": {
        "years": [2014, 2020],
        "sizes": [2000, 5000],
    },
}

# Plotting the data
plt.figure(figsize=(12, 8))

for product, values in data.items():
    years = values["years"]
    sizes = values["sizes"]
    plt.plot(years, sizes, marker='o', label=product)

# Add titles and labels
plt.title("Growth of Development Teams Over Time for Different Software Products")
plt.xlabel("Year")
plt.ylabel("Team Size")
plt.yscale("log")  # Log scale to accommodate wide range of sizes
plt.xticks(np.arange(1989, 2021, step=2))
plt.grid(True, which="both", linestyle='--', linewidth=0.5)

# Add legend
plt.legend()

# Show the plot
plt.show()
