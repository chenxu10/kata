# Perfect Information Game
# status
# base case
# transitive function
# dp(max)

# deck is a sequence of cards(c1,c2,...cn-1)
# 1 player vs dealer
# 1 dollar bet per hand


# how many times should I hit to maximize?
# subproblems suffix of ci
# number of subprobelms (n suffix)
# recurrence: BJ(i) = max(outcome(-1,0,1) + BJ(j) for all choices of j)
# dealer strategy determinstics 17



def calculate_stand_value(dealer_hand,player_sum):
    if dealer_hand > player_sum:
        return -1
    if player_sum > 21:
        return -1
    if player_sum > dealer_hand:
        return 1
    else:
        return 0
    

def test_calculate_stand_value():
    assert calculate_stand_value(11,10) == -1
    assert calculate_stand_value(11,22) == -1
    assert calculate_stand_value(11,15) == 1

test_calculate_stand_value()