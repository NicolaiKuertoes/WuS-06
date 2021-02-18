chi = sum([((gummibaerchen.Beobachtet[i] - gummibaerchen.Erwartet[i])**2) / gummibaerchen.Erwartet[i] for i in range(len(gummibaerchen.Sorte))])

chi
