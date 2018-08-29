class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        if i == len(bits) - 1:
            return True
        else:
            return False


if __name__ == '__main__':
    bits = [1, 0, 0]
    print(Solution().isOneBitCharacter(bits))