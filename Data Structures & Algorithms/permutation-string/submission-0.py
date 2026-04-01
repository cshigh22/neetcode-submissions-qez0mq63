class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            s2_count[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                s2_count[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(s1):
                if s1_count == s2_count:
                    return True
        return False           