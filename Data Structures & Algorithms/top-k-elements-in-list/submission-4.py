class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        res = []
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
            
        sorted_dict = sorted(dictionary, key = dictionary.get, reverse = True) 
        for key in sorted_dict:
            res.append(key)
            k -= 1
            if k == 0:
                break
        return res
