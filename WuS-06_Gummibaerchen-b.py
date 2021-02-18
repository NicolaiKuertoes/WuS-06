import pandas as pd

h0 =  int(750 / 6)
gummibaerchen = {
    'Sorte': ['Ananas', 'Himbeer', 'Apfel', 'Erdbeere', 'Orange', 'Zitrone'],
    'Beobachtet': [135, 114, 130, 141, 105, 125],
    'Erwartet': [h0]*6
}

gummibaerchen = pd.DataFrame(gummibaerchen)

gummibaerchen
