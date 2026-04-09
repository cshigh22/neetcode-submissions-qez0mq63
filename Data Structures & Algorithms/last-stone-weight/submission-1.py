class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)

            if y > x:
                y = -(y-x)
                heapq.heappush(stones, y)
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
