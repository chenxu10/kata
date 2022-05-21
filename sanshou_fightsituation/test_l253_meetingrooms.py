# shuangzhi zheng saomiaoxian
import heapq

def minMeetingRooms(intervals):
    h = []
    intervals.sort()
    
    for i in intervals:
        if h == [] or h[0] > i[0]:
            heapq.heappush(h, i[1])
        else:
            heapq.heapreplace(h, i[1])
    return len(h)
    
def test_minMeetingRooms():
    intervals = [[0,5],[2,4]]
    print(minMeetingRooms(intervals))
    assert minMeetingRooms([[0,5],[2,4]]) == 2

if __name__ == '__main__':
    test_minMeetingRooms()