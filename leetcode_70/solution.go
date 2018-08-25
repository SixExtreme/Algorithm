package main

func climbStairs(n int) int {
	if n <= 2 {
		return n
	} else {
		dp0, dp1 := 1, 2
		for i := 2; i < n; i += 1 {
			dp0, dp1 = dp1, dp0 + dp1
		}
		return dp1
	}
}