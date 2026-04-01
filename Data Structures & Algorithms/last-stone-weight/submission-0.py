class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            biggest = heapq.heappop(stones)
            biggest2 = heapq.heappop(stones)

            if biggest < biggest2:
                heapq.heappush(stones, biggest - biggest2)
        stones.append(0)
        return abs(stones[0])
