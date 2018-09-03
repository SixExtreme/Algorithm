class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        i, k = 0, len(flowerbed)
        while i < k:
            if flowerbed[i] == 1:
                i += 2
            else:
                lp = i - 1 < 0 or flowerbed[i - 1] == 0
                rp = i + 1 >= k or flowerbed[i + 1] == 0
                if lp and rp:
                    n -= 1
                    flowerbed[i] = 1
                i += 1 + (i + 1 < k and flowerbed[i + 1] == 0)
            if n == 0:
                return True
        return False


if __name__ == '__main__':
    flowerbed = [0, 1, 0, 1, 0, 1, 0, 0]
    print(Solution().canPlaceFlowers(flowerbed, 1))
