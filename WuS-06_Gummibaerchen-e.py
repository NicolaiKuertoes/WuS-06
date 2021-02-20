import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

# generate evenly spaced numbers over a specified interval
x = np.linspace(0, 20 ,100)

# probability density function evaluated at x
y = chi2.pdf(x, 5)

# plot density function
plt.plot(x, y, label='Dichtefunktion $\chi^2$')

# plot vertical lines at "untereGrenze" and "obereGrenze"
plt.vlines([untereGrenze, obereGrenze], [0, 0], [0.16, 0.16], colors='red', label='Grenzen des Annahmebereichs')

# plot vertical line for chi^2-value
plt.vlines(chi, [0], [0.16], colors='green', label='Prüfgröße')

# set the label for x-axis
plt.xlabel('x')

# set the label for y-axis
plt.ylabel('y')

# set a title for the axis
plt.title('$\chi^2$ Verteilung mit Annahmebereich')

# Set label locations.
plt.xticks(np.arange(0, 21, step=1))
plt.yticks(np.arange(0, 0.2, step=.01))

# configure the grid lines
plt.grid()

# place a legend on the axes.
plt.legend(loc='best')

# display all figures.
plt.show()
