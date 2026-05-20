class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        res = 0
        q = deque()

        while maxHeap or q:
            res += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, res + n])
            
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        return res