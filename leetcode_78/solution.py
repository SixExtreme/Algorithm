from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # solution 1 递归
        # n, subs = len(nums), []
        #
        # def helper(i: int, tmp: List):
        #     subs.append(tmp)
        #     for j in range(i, n):
        #         helper(j + 1, [*tmp, nums[j]])
        #
        # helper(0, [])
        # return subs

        # solution 2 迭代
        # n, subs = len(nums), [[]]
        # for i in range(n):
        #     k = len(subs)
        #     for j in range(k):
        #         tmp = [*subs[j], nums[i]]
        #         subs.append(tmp)
        # return subs

        # solution 3 位图
        # 位图的标记和数组顺序是反的
        n, k = len(nums), 2 ** len(nums)
        subs = [[] for _ in range(k)]
        for i in range(n):
            for j in range(k):
                print(bin(j), i, (j >> i) & 1)
                if (j >> i) & 1:
                    subs[j].append(nums[i])
        return subs


def test_solution():
    res = Solution().subsets([1, 2, 3])
    assert len(res) == 7
