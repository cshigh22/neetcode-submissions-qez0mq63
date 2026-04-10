class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heap.append(-i)

        heapq.heapify(heap)

        while k > 1:
            heapq.heappop(heap)
            k -= 1
        return -heapq.heappop(heap)