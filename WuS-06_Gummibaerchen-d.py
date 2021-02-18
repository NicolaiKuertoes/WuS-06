from scipy.stats import chi2
alpha = 0.01
df = len(gummibaerchen.Sorte) - 1
untereGrenze = chi2.ppf(q=alpha, df = df)
obereGrenze = chi2.ppf(q=1-alpha, df = df)
h0angenommen = untereGrenze <= chi <= obereGrenze

print('Die Grenzen für den Annahmebereich sind ({:.2f}, {:.2f})'.format(untereGrenze, obereGrenze))
if h0angenommen:
    print('Die H0 Hypothese wird angenommen')
else:
    print('Die H0 Hypothese wird abgelehnt')
