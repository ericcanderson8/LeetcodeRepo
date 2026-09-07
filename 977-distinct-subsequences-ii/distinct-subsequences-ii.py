class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # This array tracks the number of distinct subsequences 
        # ending with each letter ('a' through 'z').
        ends_with = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")

            # 1. Calculate the new total subsequences that can end with this character:
            #    Take the sum of all current distinct subsequences + 1 (for the character by itself).
            # 2. Automatically overwrite the old count for this letter.
            ends_with[idx] = (sum(ends_with) + 1) % MOD

        # The final answer is the sum of all distinct subsequences ending in any letter.
        return sum(ends_with) % MOD