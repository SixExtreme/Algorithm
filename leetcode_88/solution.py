class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # i, j = m - 1, n - 1
        # while j >= 0:
        #     if i < 0:
        #         nums1[j] = nums2[j]
        #         j -= 1
        #     elif nums1[i] < nums2[j]:
        #         nums1[i + j + 1] = nums2[j]
        #         j -= 1
        #     else:
        #         nums1[i + j + 1] = nums1[i]
        #         i -= 1

        # k = len(nums1) - 1
        # i, j = m - 1, n - 1
        # while j > -1:
        #     if i < 0 or nums1[i] < nums2[j]:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #     else:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     k -= 1

        k = len(nums1) - 1
        i, j = m - 1, n - 1
        while j > -1:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == '__main__':
    nums1 = [2, 0]
    nums2 = [1]
    Solution().merge(nums1, 1, nums2, 1)
    print(nums1)