from typing import Tuple
import numpy as np
from scipy.stats import chisquare, chi2, chi2_contingency

def kontingenztafel_test(kontingenztafel: [[float]]) -> Tuple[float, float, float]:
    '''
    Führe einen Chi-Quadrat-Test mit der Kontingenztafel durch
    
    Arguments:
        kontingenztafel -- Die Kontingenztafel (bspw. Vierfeldertafel)
    Returns:
        pruefgroesse    -- Die Prüfgröße des Chi-Quadrat-Tests
        freiheitsgrade  -- Die Anzahl der Freiheitsgrade
        p_Wert          -- Der aus dem Chi-Quadrat-Test ermittelte p-Wert
    '''
    
    pruefgroesse = 0
    p_Wert = 0
    freiheitsgrade = 0
    
    # YOUR CODE HERE
    
    # print warning if the rule of thumb does not apply
    for cell in kontingenztafel:
        for value in cell:
            if not value >= 5:
                print('Die Prüfgröße kann nicht als chi^2-verteilt angesehen werden, da nicht alle Werte größer oder gleich 5 sind.')
    
    # convert kontingenztafel to numpy array for convenience
    kontingenztafel = np.array(kontingenztafel)
    
    # calculate degrees of freedom
    freiheitsgrade = (kontingenztafel.shape[0] - 1) * (kontingenztafel.shape[1] - 1)
    
    # calculate the total
    obs_total = sum([sum(i) for i in kontingenztafel])
    
    # calculate sum of each row
    obs_sum_rows = kontingenztafel.sum(axis=1)
    
    # calculate sum of each column
    obs_sum_cols = kontingenztafel.sum(axis=0)
    
    # convert multidimensional array to one-dim. array
    obs = np.concatenate(kontingenztafel)
    
    # empty array for expected values
    exp = []
    
    # calculate expected values and add them to exp
    for i in range(len(kontingenztafel)):
        for k in range(len(kontingenztafel[0])):
            exp.append((obs_sum_rows[i] * obs_sum_cols[k]) / obs_total)
            
    # convert exp to numpy array for convenience
    exp = np.array(exp)
    
    # calculate chi^2 and p ----------- I have no clue what ddof exactly does, however... it works!
    pruefgroesse, p_Wert = chisquare(obs, exp, ddof=freiheitsgrade + 1)
    
    # return all calculated values as a tuple
    return pruefgroesse, freiheitsgrade, p_Wert


# Aufruf mit Beispiel aus der Vorlesung
pruefgroesse, freiheitsgrade, p_Wert = kontingenztafel_test([[17, 38], [18, 7]])
# Ausgabe der Werte
print(pruefgroesse, freiheitsgrade, p_Wert)
