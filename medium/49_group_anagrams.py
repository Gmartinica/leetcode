class Solution:
    def createCharDict(self, word: str) -> dict:
        anaDict = {}
        for c in word:
            if c in anaDict:
                anaDict[c] += 1
            else:
                anaDict[c] = 1
        return anaDict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use the sorted string as the key for each group of anagrams
        resultDict = {}
        for word in strs:
            # Create a character count dictionary for the current word
            wordDict = self.createCharDict(word)
            # Sort the dictionary by key and convert to a tuple to use as a hashable key
            key = tuple(sorted(wordDict.items()))
            # Add the current word to the group of anagrams with the same key
            if key in resultDict:
                resultDict[key].append(word)
            else:
                resultDict[key] = [word]
        
        # Convert the result dictionary to a list of lists
        result = []
        for group in resultDict.values():
            result.append(group)
        
        return result
