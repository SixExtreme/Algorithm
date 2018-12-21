package main

import "fmt"

func removeElement(nums []int, val int) int {
	i := 0
	for i < len(nums) {
		if nums[i] != val {
			i++
		} else {
			nums = append(nums[:i], nums[i+1:]...)
		}
	}
	return len(nums)
}

func main()  {
	nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	fmt.Println(removeElement(nums, 2))
}