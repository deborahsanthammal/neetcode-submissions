class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        for letter in s:
            if letter not in s_count:
                s_count[letter] = 1
            else:
                s_count[letter] += 1

        t_count = {}
        for letter in t:
            if letter not in t_count:
                t_count[letter] = 1
            else:
                t_count[letter] += 1

        for k in s_count:
            if k not in t_count:
                return False
            if t_count[k] != s_count[k]:
                return False
        return True
            
