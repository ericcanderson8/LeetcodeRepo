class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # we have a set of all words, if 
        # n^2 issue 
        # iterate through list of words, and check from i to end, if any words go into it. 

        wordBank = set(words)
        output = []
        outputSet = set()
        
        for word in words:
            q = deque([0])
            visited = set()
            while len(q) > 0:
                item = q.popleft()
                for i in range(item, len(word)+1):
                    if word[item:i] in wordBank and word != word[item:i] and i not in visited:
                        if i == len(word) and word not in outputSet:
                            output.append(word)
                            outputSet.add(word)
                            break
                        visited.add(i)
                        q.append(i)
        
        return output


        