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