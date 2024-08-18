class Solution:
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0
        res = []
        
        # Iterate through both strings until we reach the end of one of them
        while i < len(word1) and j < len(word2):
            res.append(word1[i])  # Append character from word1
            res.append(word2[j])  # Append character from word2
            i += 1
            j += 1
        
        # If there are remaining characters in word1 or word2, append them
        res.append(word1[i:])  # Append the rest of word1, if any
        res.append(word2[j:])  # Append the rest of word2, if any
        
        return "".join(res)  # Join list to form the final string
