# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_c = defaultdict(int)
        t_w = defaultdict(int)
        for l in t:
            t_c[l] += 1
        need = len(t_c)

        have = 0
        l = 0
        res, reslen = [-1, -1], float('infinity')
        for r in range(len(s)):
            c = s[r]
            t_w[c] += 1
            if c in t and t_w[c] == t_c[c]:
                have += 1
            while have >= need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                d = s[l]
                t_w[d] -= 1
                if d in t and t_w[d] < t_c[d]:
                    have -= 1
                l += 1
        return s[res[0]: res[1] + 1] if reslen != float('infinity') else ""

            
        