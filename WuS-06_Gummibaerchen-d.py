from scipy.stats import chi2

# given value
alpha = 0.01

# calculate lower bounds
untereGrenze = chi2.ppf(q = alpha, df = 5)

# calculate upper bounds
obereGrenze = chi2.ppf(q = 1 - alpha, df = 5)

# check if 𝜒2 exceeds the boundaries
 h0angenommen = untereGrenze <= chi <= obereGrenze

print('Die Grenzen für den Annahmebereich sind ({:.2f}, {:.2f})'.format(untereGrenze, obereGrenze))
if h0angenommen:
    print('Die H0 Hypothese wird angenommen')
else:
    print('Die H0 Hypothese wird abgelehnt')
