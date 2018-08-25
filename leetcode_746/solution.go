package main;

func minCostClimbingStairs(cost []int) int {
	n := len(cost)
	if n == 0 {
		return 0
	}
	dp0, dp1 := 0, 0
	var step2 int
	var step1 int
	for i := 2; i < n + 1; i += 1 {
		step2 = dp0 + cost[i - 2]
		step1 = dp1 + cost[i - 1]
		dp0 = dp1
		if step2 < step1 {
			dp1 = step2
		} else {
			dp1 = step1
		}
	}
	return dp1
}