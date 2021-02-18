# calculate chi^2 with Σ((o-e)²)/e, where o is the observed value and e is the expected value
chi = sum([((gummibaerchen.Beobachtet[i] - gummibaerchen.Erwartet[i])**2) / gummibaerchen.Erwartet[i] for i in range(len(gummibaerchen.Sorte))])

chi
