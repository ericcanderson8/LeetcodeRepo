class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordListSet = set(wordList)
        if endWord not in wordListSet:
            return []

        backtrack = defaultdict(list)
        seen = set([beginWord])

        # matches in wordListSet
        # you have to break apart all possibliites of the word
        def matches(word, wordListSet, current_level_seen, backtrack):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(len(word)):
                for char in alphabet:
                    checkWord = word[:i] + char + word[i+1:]
                    if checkWord in wordListSet and checkWord not in seen:
                        if checkWord not in current_level_seen:
                            current_level_seen.add(checkWord)
                            output.append(checkWord)
                        backtrack[checkWord].append(word)
            

        queue = deque([beginWord])
        found = False


        while queue:
            current_level_seen = set()
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    found = True
                
                output = []
                matches(word, wordListSet, current_level_seen, backtrack)
                # check what matches it has to the wordlist

                for nextWord in output:
                    queue.append(nextWord)

            if found == True:
                break
            seen.update(current_level_seen)

        print(backtrack)
        output = []
        def dfs(word, currPath):
            currPath = list(currPath)
            currPath.append(word)

            if word == beginWord:
                output.append(currPath[::-1])
                return
            
            for nextWord in backtrack[word]:
                dfs(nextWord, currPath)

        
        dfs(endWord, [])
        return output
        # go to the last element, and dfs our way to the beginning
    # so now, we begin at the last element in the 

