from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        SIZE = len(words[0])
        TOTAL_WORDS = len(words)
        WINDOW_LEN = SIZE * TOTAL_WORDS
        
        if WINDOW_LEN > len(s):
            return []

        # Target dictionary we want to match
        target_dict = Counter(words)
        output = []

        # Outer loop: offsets from 0 to SIZE-1
        for i in range(SIZE):
            l = i
            r = i
            current_window = Counter()
            
            # 1. Initialize the FIXED window up to WINDOW_LEN
            # We stop when r has moved forward by exactly WINDOW_LEN (or we hit string end)
            while r < i + WINDOW_LEN and r + SIZE <= len(s):
                word = s[r : r + SIZE]
                current_window[word] += 1
                r += SIZE
                
            # Check if this very first window is a match
            if current_window == target_dict:
                output.append(l)
                
            # 2. Slide the FIXED window one word at a time
            while r + SIZE <= len(s):
                # Add the new word entering on the right
                right_word = s[r : r + SIZE]
                current_window[right_word] += 1
                r += SIZE
                
                # Remove the old word falling out on the left
                left_word = s[l : l + SIZE]
                current_window[left_word] -= 1
                
                # Clean up zero counts so direct dictionary comparison works
                if current_window[left_word] == 0:
                    del current_window[left_word]
                    
                l += SIZE
                
                # If the dictionaries match, we found a valid starting index!
                if current_window == target_dict:
                    output.append(l)
                    
        return output