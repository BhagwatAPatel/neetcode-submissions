class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {} # Declare a dict
        for a, b in zip(s, t):
            count[a] = count.get(a, 0) + 1 # start -> end
            count[b] = count.get(b, 0) - 1 # end -> start
        return all(v == 0 for v in count.values())
    