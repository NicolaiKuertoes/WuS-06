import math

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
    
    # lists to store left and right P-Values
    p_Left = []
    p_Right = []
    
    # write all values in a single list for convenience e.g. [[4,1], [2,2]] --> [4,1,2,2]
    vft = [vierfeldertafel[i][k] for i in range(len(vierfeldertafel)) for k in range(len(vierfeldertafel[0]))]
    
    # +++++++++ MY DEBUGGER +++++++++
    '''
    Simply prints out some values to ckeck them.
    '''
    def debug():
        print("Tafeln:", len(p_Werte))
        print("P-Start:", p_Start)
        print("P-Werte:", p_Werte)
    
    # calculate the probability of given contingency table
    def P(vft_tmp: [float]) -> float:
        n_vft = sum(vft_tmp)
        return (math.factorial(vft_tmp[0]+vft_tmp[1])*math.factorial(vft_tmp[2]+vft_tmp[3])*math.factorial(vft_tmp[0]+vft_tmp[2])*math.factorial(vft_tmp[1]+vft_tmp[3]))\
            /(math.factorial(n_vft)*math.factorial(vft_tmp[0])*math.factorial(vft_tmp[1])*math.factorial(vft_tmp[2])*math.factorial(vft_tmp[3]))
    
    # calculate probability of contingency tables to the left
    def fisher_left(vft_in: [float]):
        vft_out = [i for i in vft_in] # can't write "vft_out = vft_in" --> idk why, but it would change my vft 
        while vft_out[1] > 0 and vft_out[2] > 0:
            vft_out[0] += 1
            vft_out[1] -= 1
            vft_out[2] -= 1
            vft_out[3] += 1
            p_Left.append(P(vft_out))
    
    # calculate probability of contingency tables to the right
    def fisher_right(vft_in: [float]):
        vft_out = [i for i in vft_in] # can't write "vft_out = vft_in" --> idk why, but it would change my vft
        while vft_out[0] > 0 and vft_out[3] > 0:
            vft_out[0] -= 1
            vft_out[1] += 1
            vft_out[2] += 1
            vft_out[3] -= 1
            p_Right.append(P(vft_out))

    # get the starting P-Value
    p_Start = P(vft)
    
    # get all P-Values of the left side then reverse the list for visual convenience
    fisher_left(vft)
    p_Left.reverse()
    
    # get all P-Values of the right side
    fisher_right(vft)
    
    # concatenate all P-Values from left to right
    p_Werte = sum([p_Left, [p_Start] ,p_Right], [])
    
    # calculate the single P Value
    p_Wert = sum([i for i in p_Werte if i <= p_Start])
    
    # +++ MY DEBUGGER +++
    #debug()
    
    # return the resulting P-Value of the two-tailed Fisher exact test
    return p_Wert


# YOUR CODE HERE --- added some custom contingency tables for testing
#vierfeldertafel = [[4, 1],[1, 4]]
#vierfeldertafel = [[18, 2],[11, 9]]
#vierfeldertafel = [[3, 0],[0, 5]]
#vierfeldertafel = [[0, 5],[2, 5]]
#vierfeldertafel = [[5, 0],[0, 5]]

# given contingency table
vierfeldertafel = [[4, 1],[2, 2]]

# show my value vs pythons value
fisher_exakt(vierfeldertafel), stats.fisher_exact(vierfeldertafel)[1]
