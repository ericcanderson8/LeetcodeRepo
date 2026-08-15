from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        
        class Node:
            __slots__ = ['size', 'prefixChar', 'suffixChar', 'prefixLen', 'suffixLen', 'maxLen']

            def __init__(self):
                self.size = 0
                self.prefixChar = ""
                self.suffixChar = ""
                self.prefixLen = 0
                self.suffixLen = 0
                self.maxLen = 0

        n = len(s)
        tree = [Node() for _ in range(4 * n)]
        
        def merge(treeIndex, leftIndex, rightIndex):
            tree[treeIndex].size = tree[leftIndex].size + tree[rightIndex].size
            tree[treeIndex].suffixChar = tree[rightIndex].suffixChar
            tree[treeIndex].prefixChar = tree[leftIndex].prefixChar
            
            tree[treeIndex].suffixLen = tree[rightIndex].suffixLen
            tree[treeIndex].prefixLen = tree[leftIndex].prefixLen
            tree[treeIndex].maxLen = max(tree[leftIndex].maxLen, tree[rightIndex].maxLen)

            if tree[leftIndex].suffixChar == tree[rightIndex].prefixChar:
                bridge_len = tree[leftIndex].suffixLen + tree[rightIndex].prefixLen
                tree[treeIndex].maxLen = max(tree[treeIndex].maxLen, bridge_len)

                if tree[leftIndex].prefixLen == tree[leftIndex].size:
                    tree[treeIndex].prefixLen = tree[leftIndex].size + tree[rightIndex].prefixLen
                
                if tree[rightIndex].suffixLen == tree[rightIndex].size:
                    tree[treeIndex].suffixLen = tree[rightIndex].size + tree[leftIndex].suffixLen

        def build(treeIndex, l, r):
            if l == r: 
                tree[treeIndex].size = 1
                tree[treeIndex].suffixLen = 1
                tree[treeIndex].suffixChar = s[l]
                tree[treeIndex].prefixLen = 1
                tree[treeIndex].prefixChar = s[l]
                tree[treeIndex].maxLen = 1
                return 
            
            mid = (l + r) // 2
            leftIndex = treeIndex * 2 + 1
            rightIndex = treeIndex * 2 + 2
            
            build(leftIndex, l, mid)
            build(rightIndex, mid + 1, r)

            # Replaced the duplicate logic with our helper
            merge(treeIndex, leftIndex, rightIndex)
            
        def update(treeIndex, l, r, targetIndex, newChar):
            if l == r:
                tree[treeIndex].prefixChar = newChar
                tree[treeIndex].suffixChar = newChar
                return
            
            mid = (l + r) // 2
            leftIndex = treeIndex * 2 + 1
            rightIndex = treeIndex * 2 + 2
            
            if targetIndex <= mid:
                update(leftIndex, l, mid, targetIndex, newChar)
            else:
                update(rightIndex, mid + 1, r, targetIndex, newChar)
                
            merge(treeIndex, leftIndex, rightIndex)

        # --- EXECUTION ---
        
        # 1. Initialize the tree with the original string
        build(0, 0, n - 1)
        
        ans = []
        
        # 2. Process each query
        for i in range(len(queryIndices)):
            targetIndex = queryIndices[i]
            newChar = queryCharacters[i]
            
            # Update the segment tree in O(log n) time
            update(0, 0, n - 1, targetIndex, newChar)
            
            # The root node (index 0) always holds the max length for the whole string
            ans.append(tree[0].maxLen)
            
        return ans