from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs.sort(key=lambda cost: cost[0] - cost[1])
        # print(costs)
        # ans, k = 0, len(costs) // 2
        # for i in range(k):
        #     ans += costs[i][0] + costs[i + k][1]
        # return ans

        # 正排倒排都一样
        # 到头来选择还是不变

        costs.sort(key=lambda cost: cost[1] - cost[0])
        ans, k = 0, len(costs) // 2
        for i in range(k):
            ans += costs[i][1] + costs[i + k][0]
        return ans


def test_solution():
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    assert Solution().twoCitySchedCost(costs) == 110
