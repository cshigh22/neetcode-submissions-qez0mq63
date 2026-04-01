class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stack = []
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1 
            else:
                hashmap[i] = 1

        sorted_hash = sorted(hashmap, key = hashmap.get, reverse = True)
        for i in sorted_hash:
            stack.append(i)
            if len(stack) > k:
                stack.pop()
        return stack
        
