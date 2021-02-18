import math

def fisher_exakt(vierfeldertafel) -> float:
    '''
    Führe den zweiseitigen Fisher-Test für eine Vierfeldertafel aus
    
    Arguments:
        vierfeldertafel -- Die Vierfeldertafel
    Returns:
        p_Wert          -- Der p-Wert 
    '''
    # YOUR CODE HERE
    
    p_Wert = 0
    
    # lists to store left and right P-Values
    p_Left = []
    p_Right = []
    
    # write all values in a single list for convenience
    vft = []
    for i in range(len(vierfeldertafel)):
        for k in range(len(vierfeldertafel[0])):
            vft.append(vierfeldertafel[i][k])
    
    # calculate the probability of given contingency table ---------------------- HELPER
    def P(vft_tmp: [float]) -> float:
        n_vft = sum(vft_tmp)
        return (math.factorial(vft_tmp[0]+vft_tmp[1])*math.factorial(vft_tmp[2]+vft_tmp[3])*math.factorial(vft_tmp[0]+vft_tmp[2])*math.factorial(vft_tmp[1]+vft_tmp[3]))\
            /(math.factorial(n_vft)*math.factorial(vft_tmp[0])*math.factorial(vft_tmp[1])*math.factorial(vft_tmp[2])*math.factorial(vft_tmp[3]))
    
    # calculate probability of contingency tables to the left
    def fisher_left(vft_in: [float]):
        vft_out = [i for i in vft_in]
        vft_min = vft_out.index(min(vft_out))
        while not 0 in vft_out:
            vft_out[0] += 1
            vft_out[1] -= 1
            vft_out[2] -= 1
            vft_out[3] += 1
            p_Left.append(P(vft_out))
    
    # calculate probability of contingency tables to the right
    def fisher_right(vft_in: [float]):
        vft_out = [i for i in vft_in]
        vft_max = vft_out.index(max(vft_out))
        while not 0 in vft_out:
            vft_out[0] -= 1
            vft_out[1] += 1
            vft_out[2] += 1
            vft_out[3] -= 1
            p_Right.append(P(vft_out))
    
    # get the starting P-Value
    p_Start = P(vft)
    
    # get all P-Values of the left side
    fisher_left(vft)
    # reverse left P-Values list
    p_Left.reverse()
    
    # get all P-Values of the right side
    fisher_right(vft)
    
    # concatenate all P-Values from left to right
    p_Werte = sum([p_Left, [P(vft)] ,p_Right], [])
    
    # calculate the single P Value
    p_Wert = sum([i for i in p_Werte if i <= p_Start])
    
    # return the resulting P-Value of the two-tailed Fisher exact test
    return p_Wert


# YOUR CODE HERE
  
vierfeldertafel = [[4, 1],[2, 2]]
#vierfeldertafel = [[4, 1],[1, 4]]
#vierfeldertafel = [[18, 2],[11, 9]]

fisher_exakt(vierfeldertafel), stats.fisher_exact(vierfeldertafel)
