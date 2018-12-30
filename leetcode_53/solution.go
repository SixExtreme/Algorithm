package main

func maxSubArray(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	sum, max := 0, nums[0]
	for _, x := range nums {
		sum += x
		if x > sum {
			sum = x
		}
		if sum > max {
			max = sum
		}
	}
	return max
}

//func maxSubArray(nums []int) int {
//	if len(nums) == 0 {
//		return 0
//	}
//
//	dp := make([]int, len(nums))
//	dp[0] = nums[0]
//
//	max := nums[0]
//	for i := 1; i < len(nums); i++ {
//		dp[i] = dp[i - 1] + nums[i]
//		if dp[i] < nums[i] {
//			dp[i] = nums[i]
//		}
//		if dp[i] > max {
//			max = dp[i]
//		}
//	}
//
//	return max
//}

func main()  {

}