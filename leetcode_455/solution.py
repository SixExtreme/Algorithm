class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i, j = 0, 0
        m, n = len(g), len(s)

        while i < m and j < n:
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    g = [7, 8, 9, 10]
    s = [5, 6, 7, 8]
    print(Solution().findContentChildren(g, s))

