class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        stack = []

        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        sorted_dict = sorted(dictionary, key = dictionary.get, reverse = True)

        for i in sorted_dict:
            stack.append(i)

            if len(stack) > k:
                stack.pop()
        return stack