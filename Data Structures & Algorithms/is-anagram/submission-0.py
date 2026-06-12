class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable_s = {}
        hashTable_t = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in hashTable_s:
                hashTable_s[i] += 1
            else:
                hashTable_s[i] = 1

        for i in t:
            if i in hashTable_t:
                hashTable_t[i] += 1
            else:
                hashTable_t[i] = 1

        if hashTable_s == hashTable_t:
            return True

        return False
