package main

func climbStairs(n int) int {
	if n <= 2 {
		return n
	} else {
		dp1, dp2 := 1, 2
		for i := 2; i < n; i += 1 {
			dp1, dp2 = dp2, dp1 + dp2
		}
		return dp2
	}
}