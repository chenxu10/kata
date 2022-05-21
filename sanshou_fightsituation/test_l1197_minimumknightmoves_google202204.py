"""
Minimum number of steps
"""
from collections import deque

# Induction we know how to solve shortest steps in a subgraph
# with horse can be reached 
def minKnightMoves(x,y):
    pass
    # offset

    # is_target

    # next_x,next_y whether in seen

# T:O(max(|x|,|y|)^2)       
# S:O(max(|x|,|y|)^2)       

def test_minknightmoves():
    assert minKnightMoves(2,1) == 1
    assert minKnightMoves(5,5) == 4