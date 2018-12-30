package main

//func majorityElement(nums []int) int {
//	count, major := 1, nums[0]
//	for i := 1; i < len(nums); i++ {
//		if count == 0 {
//			major = nums[i]
//			count++
//		} else {
//			if nums[i] == major {
//				count++
//			} else {
//				count--
//			}
//		}
//	}
//	return major
//}

func majorityElement(nums []int) int {
	count, major := 1, nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] == major {
			count++
		} else {
			if count != 0 {
				count--
			} else {
				count, major = 1, nums[i]
			}
		}
	}
	return major
}