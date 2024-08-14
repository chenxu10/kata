from typing import List

def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    def merge_skylines(left, right):
        "O(n)"
        merged = []
        h1, h2 = 0, 0
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            x = 0
            # determine the next x-coordinates
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, h2 = right[j]
                j += 1
            else:
                x, h1 = left[i]
                _, h2 = right[j]
                i += 1
                j += 1
            # Try to add in a point with maximum height
            max_h = max(h1, h2)
            if not merged or max_h != merged[-1][1]:
                merged.append([x, max_h])
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged
    
    def divide(buildings):
        if not buildings:
            return []

        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        mid = len(buildings) // 2
        left_skyline = divide(buildings[:mid])
        right_skyline = divide(buildings[mid:])

        return merge_skylines(left_skyline, right_skyline)

    return divide(buildings)
    
# Problem can also be solved using scanning tree