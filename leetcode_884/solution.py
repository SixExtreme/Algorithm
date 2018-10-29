class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        map = dict()
        words = (A + ' ' + B).split()
        for w in words:
            map[w] = map.get(w, 0) + 1
        return [k for k in map if map[k] == 1]

