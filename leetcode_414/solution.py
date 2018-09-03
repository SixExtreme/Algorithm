from queue import deque

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = set(nums)
        #
        # if len(nums) < 3:
        #     return max(nums)
        #
        # nums.remove(max(nums))
        # nums.remove(max(nums))
        #
        # return max(nums)

        if len(nums) < 3:
            return max(nums)

        q = []
        for i, x in enumerate(nums):
            if not q:
                q.append(x)
            elif len(q) == 1:
                if x > q[0]:
                    q.append(x)
                if x < q[0]:
                    q.append(x)
                    q[0], q[1] = q[1], q[0]
            elif len(q) == 2:
                if x > q[1]:
                    q.append(x)
                elif q[0] < x < q[1]:
                    q.append(x)
                    q[1], q[2] = q[2], q[1]
                elif x < q[0]:
                    q.append(x)
                    q[0], q[1], q[2] = q[2], q[0], q[1]
            else:
                if x > q[2]:
                    q[0],  q[1], q[2] = q[1], q[2], x
                elif q[1] < x < q[2]:
                    q[0], q[1] = q[1], x
                elif q[0] < x < q[1]:
                    q[0] = x

        return q[-1] if len(q) < 3 else q[0]

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().thirdMax(nums))
