from typing import List, Tuple

def sweep_line_algorithm(events: List[Tuple[int, int]]) -> List[List[int]]:
    OPEN, CLOSE = 0, 1
    
    # Sort events
    events.sort(key=lambda x: (x[0], x[1]))
    
    result = []
    open_count = 0
    start = 0
    
    for time, event_type in events:
        if open_count == 0:
            start = time
        
        if event_type == OPEN:
            open_count += 1
        else:
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

# Test case
def test_sweep_line():
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    print("Test case passed!")

if __name__ == "__main__":
    test_sweep_line()
