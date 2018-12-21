package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int)  {
	k := len(nums1) - 1
	i, j := m - 1, n - 1
	for j > -1 {
		//if i < 0 {
		//	nums1[k] = nums2[j]
		//	j--
		//} else {
		//	if nums1[i] > nums2[j] {
		//		nums1[k] = nums1[i]
		//		i--
		//	} else {
		//		nums1[k] = nums2[j]
		//		j--
		//	}
		//}
		//k--

		//if i < 0 || nums2[j] > nums1[i] {
		//	nums1[k] = nums2[j]
		//	j--
		//} else {
		//	nums1[k] = nums1[i]
		//	i--
		//}
		//k--

		if i >= 0 && nums2[j] <= nums1[i] {
			nums1[k] = nums1[i]
			i--
		} else {
			nums1[k] = nums2[j]
			j--
		}
		k--
	}
}

func main() {
	num1 := []int{2, 0}
	num2 := []int{1}
	merge(num1, 1, num2, 1)
	fmt.Println(num1)
}
