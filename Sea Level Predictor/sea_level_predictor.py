import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c = 'r', alpha = 0.5)

    # Create first line of best fit
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2050)
    y1 = fit1.intercept + fit1.slope * x1
    plt.plot(x1, y1, 'k', label='Best fit line (all data)')

    # Create second line of best fit
    yr2 = df[df['Year']>=2000]
    fit2 = linregress(yr2['Year'], yr2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(yr2['Year'].min(), 2050)
    y2 = fit2.intercept + fit2.slope * x2
    plt.plot(x2, y2, 'b', label='Best fit line (year >= 2000)')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()