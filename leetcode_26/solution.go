package main

import (
	"fmt"
)

func removeDuplicates(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}

	i, j := 0, 1
	for j < len(nums) {
		if nums[j] != nums[i] {
			i, j = i + 1, j + 1
		} else {
			nums = append(nums[:i], nums[j:]...)
		}
	}

	return len(nums)
}

func main()  {
	nums := []int{1, 1, 2}
	fmt.Println(removeDuplicates(nums), nums)
}
