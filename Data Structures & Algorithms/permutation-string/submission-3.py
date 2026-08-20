class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        l = 0

        for i in s1:
            s1_count[i] = s1_count.get(i, 0) + 1

        for r in range(len(s2)):
            while (r - l) + 1 > len(s1):
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    s2_count.pop(s2[l], None)
                l += 1
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

            if s1_count == s2_count:
                return True

        return False
