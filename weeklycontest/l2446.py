from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[1] and event2[0] <= event1[1]

# Related problems
# 252. Meeting Rooms
# 253. Meeting Rooms II
# Recetangle Overlap 