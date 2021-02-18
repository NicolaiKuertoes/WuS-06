import pandas as pd

# simple calculation of expected values
exp =  int(750 / 6)

# create a pandas DataFrame
gummibaerchen = pd.DataFrame({
    'Sorte': ['Ananas', 'Himbeer', 'Apfel', 'Erdbeere', 'Orange', 'Zitrone'],
    'Beobachtet': [135, 114, 130, 141, 105, 125],
    'Erwartet': [exp]*6
})

# show the dataframe
gummibaerchen
