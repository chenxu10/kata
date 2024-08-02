"""
A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right. Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right (or all the remaining seats to that side if there are fewer than KK) remain empty.
There are currently MM diners seated at the table, the iith of whom is in seat SiSi. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
"""

def additional_sitters_infrontof_seaters(K, S):
    num_new_dinners = (S[K - 1] - S[0]) // (K + 1)
    return num_new_dinners

def additional_sitters_after_seaters(N, K, num_new_dinners):
    num_new_dinners += (N - 1) // (K + 1)

def getMaxAdditionalDinersCount(N,K,M,S):
    S.sort()
    num_new_dinners = additional_sitters_infrontof_seaters(K, S)

    for i in range(1, len(S)):
        num_new_dinners += (S[i] - S[i - 1] - K - 1) // (K + 1)

    additional_sitters_after_seaters(N, K, num_new_dinners)

    return num_new_dinners

def test_cafteria():
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    assert getMaxAdditionalDinersCount(N,K,M,S) == 3