class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_idx = {word: i for i, word in enumerate(words)}
        output = []

        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                prefix = word[:i]
                suffix = word[i:]

                # Case 1: If prefix is a palindrome, check if suffix's reverse exists
                # Condition `i != 0` prevents duplicate pair generation with Case 2
                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_to_idx and word_to_idx[rev_suffix] != idx:
                        output.append([word_to_idx[rev_suffix], idx])

                # Case 2: If suffix is a palindrome, check if prefix's reverse exists
                if i != n and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_to_idx and word_to_idx[rev_prefix] != idx:
                        output.append([idx, word_to_idx[rev_prefix]])

        return output