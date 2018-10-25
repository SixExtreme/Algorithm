class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        map = dict()
        for item in times:
            s, e, w = item[0], item[1], item[2]
            if s not in map:
                map[s] = [(e, w)]
            else:
                map[s].append((e, w))

        visit = [[False for _ in range(N + 1)] for _ in range(N + 1)]

