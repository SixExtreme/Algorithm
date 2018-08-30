class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        i, j = 0, 0
        while i < len(S) and j < len(S):
            while j < len(S) and S[i] == S[j]:
                j += 1
            if j - i >= 3:
                ret.append((i, j - 1))
            i = j
        return ret


if __name__ == '__main__':
    S = 'abcdddeeeeaabbbcd'
    print(Solution().largeGroupPositions(S))