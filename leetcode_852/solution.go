package main

import "fmt"

func peakIndexInMountainArray(A []int) int {
	l, r := 0, len(A)-1
	for l < r {
		mid := int((l + r) / 2)
		if A[mid] < A[mid+1] {
			l = mid
		} else if A[mid] < A[mid-1] {
			r = mid
		} else {
			return mid
		}
	}
	return -1
}

func main() {
	A := []int{0, 1, 0}
	ret := peakIndexInMountainArray(A)
	fmt.Println(ret)
}
