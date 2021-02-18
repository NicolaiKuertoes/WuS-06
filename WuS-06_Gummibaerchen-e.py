import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

# YOUR CODE HERE
x = np.linspace(0, 20 ,100)
y = chi2.pdf(x, 5)

plt.plot(x, y, label='Dichtefunktion $\chi^2$')
plt.vlines([chi2.ppf(q=untereGrenze, df=5), chi2.ppf(q=obereGrenze, df=5)], [0, 0], [0.16, 0.16], colors='red', label='Grenzen des Annahmebereichs')
plt.vlines([13.14], [0], [0.16], colors='green', label='Prüfgröße')
plt.xlabel('x')
plt.ylabel('y')
plt.title('$\chi^2$ Verteilung mit Annahmebereich')
plt.grid()
plt.legend(loc='best')
plt.show()
# TEXT für vertikale Linien (oben, unten)
