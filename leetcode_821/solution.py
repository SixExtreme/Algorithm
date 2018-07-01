class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n, ret = len(S), list()

        prev = float('-inf')
        for i, c in enumerate(S):
            if c == C:
                prev = i
            ret.append(i - prev)
        
        prev = float('inf')
        for i in reversed(range(n)):
            if S[i] == C:
                prev = i
            ret[i] = min(ret[i], prev - i)
        
        return ret


