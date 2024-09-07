from typing import List, Tuple
import heapq

def sweep_line_algorithm(events: List[Tuple[int, int]]) -> List[List[int]]:
    OPEN, CLOSE = 0, 1
    
    # Sort events
    events.sort(key=lambda x: (x[0], x[1]))
    
    """
    Visualization:
    
    Timeline:  |------------------------------------->
                ^   ^     ^     ^   ^     ^
    Events:    [1,O] [2,O] [3,C] [4,O] [5,C] [6,C]
                |   |     |     |   |     |
    Intervals:  |___|_____|     |___|_____|
                |___________|   |_________|
    
    O: Open event
    C: Close event
    """
    
    result = []
    open_count = 0
    start = 0
    
    for time, event_type in events:
        """
        Imagine a vertical line sweeping from left to right:
        
        |       |       |       |       |       |
        |   |___|_______|   |___|_______|       |
        |   |   |       |   |   |       |       |
        |[1,O] [2,O]  [3,C] [4,O]     [5,C]   [6,C]
        """
        if open_count == 0:
            start = time

        if event_type == OPEN:
            open_count += 1
        if event_type == CLOSE:
            open_count -= 1
        if open_count == 0:
            result.append([start, time])
         
    return result
 
# Example usage for insert interval problem
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    events = []
    OPEN, CLOSE = 0, 1

    for interval in intervals + [newInterval]:
        events.append((interval[0],OPEN))
        events.append((interval[1],CLOSE))

    return sweep_line_algorithm(events)


def insert_heap(intervals, newInterval):
    heap = [(i[0],i[1],i) for i in intervals + [newInterval]]
    heapq.heapify(heap)
    
    result = []
    while heap:
        start, end, interval = heapq.heappop(heap)
        
        if not result or start > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], end)
    
    return result

# Test case
def test_sweep_line():
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert_heap([[1,3],[6,9]],[2,5]) == [[1,5],[6,9]]
    print("Test case passed!")

if __name__ == "__main__":
    test_sweep_line()
