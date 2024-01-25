import numpy as np
import pandas as pd
from classic_ruin_problem import ruin_prob, markov_chain_probability

def test_ruin_prob():
    p = 0.45
    z = 9
    a = 10
    actual = ruin_prob(p,z,a)
    print(actual)
    expect = 0.210
    tolerance = 0.001
    assert abs(actual - expect) < tolerance

def test_ruin_prob_2():
    p = 0.5
    z = 9
    a = 10
    actual = ruin_prob(p,z,a)
    expect = 0.1
    tolerance = 0.001
    assert abs(actual - expect) < tolerance

def test_ruin_prob_3():
    Q = np.array([[1,0,0,0],
              [1/3,0,2/3,0], 
              [0,1/3,0,2/3],
              [0,0,0,1]])
    
    initial_state = np.array([[0,1,0,0]])
    stateHist=initial_state
    dfStateHist=pd.DataFrame(initial_state)
    probability = markov_chain_probability(
        initial_state, Q)
    #assert probability == 3/7
    print(probability)

if __name__ == '__main__':
    test_ruin_prob_3()