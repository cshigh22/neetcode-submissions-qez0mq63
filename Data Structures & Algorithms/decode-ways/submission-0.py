class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_back = 1  # This acts like dp[i-2] (initially dp[-1] or empty string)
        one_back = 1  # This acts like dp[i-1] (initially dp[0] for first digit)

        for i in range(1, len(s)):
            current = 0
            # If one digit is valid (1-9), add one_back
            if s[i] != '0':
                current += one_back
            
            # If two digits are valid (10-26), add two_back
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += two_back
            
            # Move our variables forward for the next loop
            two_back = one_back
            one_back = current

        return one_back