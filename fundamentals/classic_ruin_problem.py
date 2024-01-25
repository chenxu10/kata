"""
Try to solve this problem from three perspective
1. [DONE]Difference equation
2. [TODO]Random walk(simulation)
3. [DOING]Markov chain
"""
import math
import random
import numpy as np
import pandas as pd

def ruin_prob(p, z, a):
    q = 1 - p
    if p == q:
        return 1 - z/a
    else:
        return ((q/p)** a - (q/p) ** z)/((q/p)**a - 1)

def markov_chain_probability(initial_state, transition_matrix):
    stateHist=initial_state
    for x in range(100):
        initial_state = np.dot(initial_state, transition_matrix)
        stateHist=np.append(stateHist,initial_state,axis=0) 
        dfDistrHist = pd.DataFrame(stateHist) 

    return dfDistrHist