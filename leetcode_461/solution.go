package main

import (
	"fmt"
)

func hammingDistance(x int, y int) int {
	// return bits.OnesCount(uint(x ^ y))

	z := x ^ y
	ret := 0
	for z > 0 {
		z &= z - 1
		ret++
	}
	return ret
}

func main() {
	fmt.Println(hammingDistance(97, 73))
}
