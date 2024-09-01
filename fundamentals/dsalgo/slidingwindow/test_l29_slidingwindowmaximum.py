import heapq

def maxSlidingWindow(nums, k):
    """
    >>>maxSlidingWindow([1,3,-1,-3,5,3,6,7],k=3)
    [3,3,5,5,6,7]
    """
    # n = len(nums)
    # if n * k == 0:
    #     return []
    # return [max(nums[i:i + k]) for i in range(0, n - k + 1)]

    def init_output_heap(nums, k):
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        result = [-heap[0][0]]
        return heap, result
    
    def build_output(nums, k):
        for i in range(k, len(nums)):
            popheap_when_larger(nums, k, i)
        return result

    def popheap_when_larger(nums, k, i):
        heapq.heappush(heap, (-nums[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        result.append(-heap[0][0])
       
    heap, result = init_output_heap(nums, k)
    return build_output(nums, k)

if __name__ == "__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],k=3))
    print(maxSlidingWindow([1],k=1))