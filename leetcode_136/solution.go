package main

func singleNumber(nums []int) int {
	num := 0
	for _, x := range nums {
		num ^= x
	}
	return num
}
