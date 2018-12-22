package main

import "fmt"

//func searchInsert(nums []int, target int) int {
//	i := 0
//	for i < len(nums) {
//		if nums[i] < target {
//			i++
//		} else {
//			break
//		}
//	}
//	return i
//}

func searchInsert(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}

	l, h := 0, len(nums) - 1
	for l <= h {
		m := (l + h) / 2
		if nums[m] == target {
			return m
		} else if nums[m] > target {
			h = m - 1
		} else {
			l = m + 1
		}
	}

	return l
}

func main()  {
	nums := []int{1, 3, 5, 6}
	fmt.Println(searchInsert(nums, 5))
	fmt.Println(searchInsert(nums, 2))
	fmt.Println(searchInsert(nums, 7))
	fmt.Println(searchInsert(nums, 0))
}
