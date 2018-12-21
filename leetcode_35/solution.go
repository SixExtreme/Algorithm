package main

import "fmt"

func searchInsert(nums []int, target int) int {
	i := 0
	for i < len(nums) {
		if nums[i] < target {
			i++
		} else {
			break
		}
	}
	return i
}

func main()  {
	nums := []int{1, 3, 5, 6}
	fmt.Println(searchInsert(nums, 5))
	fmt.Println(searchInsert(nums, 2))
	fmt.Println(searchInsert(nums, 7))
	fmt.Println(searchInsert(nums, 0))
}
