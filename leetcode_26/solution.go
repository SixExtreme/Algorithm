package main

import (
	"fmt"
)

//func removeDuplicates(nums []int) int {
//	if len(nums) <= 1 {
//		return len(nums)
//	}
//
//	i, j := 0, 1
//	for j < len(nums) {
//		if nums[j] != nums[i] {
//			i, j = i + 1, j + 1
//		} else {
//			nums = append(nums[:i], nums[j:]...)
//		}
//	}
//
//	return len(nums)
//}

//func removeDuplicates(nums []int) int {
//	if len(nums) <= 1 {
//		return len(nums)
//	}
//
//	i := 0
//	for j := 1; j < len(nums); j++ {
//		if nums[j] != nums[i] {
//			nums[i + 1] = nums[j]
//			i++
//		}
//	}
//	return i + 1
//}

func removeDuplicates(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}

	k := 1
	for j := 1; j < len(nums); j++ {
		if nums[j] != nums[k - 1] {
			nums[k] = nums[j]
			k++
		}
	}
	return k
}


func main()  {
	nums := []int{0,0,1,1,1,2,2,3,3,4}
	fmt.Println(removeDuplicates(nums), nums)
}
