class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            _sum = numbers[i] + numbers[j]
            if _sum == target:
                return (i + 1, j + 1)
            else:
                if _sum < target:
                    i += 1
                else:
                    j -= 1

if __name__ == '__main__':
    numbers = [-1, 0]
    print(Solution().twoSum(numbers, -1))