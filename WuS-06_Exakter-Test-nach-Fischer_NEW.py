import math
from math import factorial as fak

def fisher_exakt(vierfeldertafel) -> float:
    '''
    Führe den zweiseitigen Fisher-Test für eine Vierfeldertafel aus
    
    Arguments:
        vierfeldertafel -- Die Vierfeldertafel
    Returns:
        p_Wert          -- Der p-Wert 
    '''
    p_Wert = 0
    # YOUR CODE HERE
    
    # flatten 2D list to 1D list for convenience
    vft = sum([vierfeldertafel[0], vierfeldertafel[1]], [])
    
    # calculate the probability of given contingency table
    def calc_P(vft_in: [float]) -> float:
        a, b, c, d = vft_in
        n = sum([a, b, c, d])
        return (fak(a+b)*fak(c+d)*fak(a+c)*fak(b+d))/(fak(n)*fak(a)*fak(b)*fak(c)*fak(d))
    
    # run to left and right and calculate the P-Value for each table
    def runFisher(vft_in: [float]) -> float:
        p_List = [] # list to store all P-Values which are less than the starting P-Value
        # run left
        a, b, c, d = vft_in
        while b > 0 and c > 0:
            a,d = a+1, d+1
            b,c = b-1, c-1
            p_Tmp = calc_P([a,b,c,d])
            if p_Tmp <= p_Start : p_List.append(p_Tmp)
        # run right    
        a, b, c, d = vft_in
        while a > 0 and d > 0:
            a,d = a-1, d-1
            b,c = b+1, c+1
            p_Tmp = calc_P([a,b,c,d])
            if p_Tmp <= p_Start : p_List.append(p_Tmp)
        return sum(p_List) + p_Start
    
    # starting P-Value
    p_Start = calc_P(vft)
    
    # sum of all P-Values which are smaller than the starting P-Value
    p_Wert = runFisher(vft)
    
    return p_Wert

# YOUR CODE HERE
vierfeldertafel = [[5, 0],[0, 5]]
fisher_exakt(vierfeldertafel), stats.fisher_exact(vierfeldertafel)[1]
