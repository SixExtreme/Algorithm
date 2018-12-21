package main

import "fmt"

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i > -1; i-- {
		if digits[i] + 1 > 9 {
			digits[i] = 0
		} else {
			digits[i] += 1
			return digits
		}
	}
	return append([]int{1}, digits...)
}

func main() {
	digits := []int{9, 9}
	fmt.Println(plusOne(digits))
}