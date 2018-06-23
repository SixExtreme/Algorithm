package main

import "fmt"

func flipAndInvertImage(A [][]int) [][]int {
	for _, row := range A {
		n := len(row)
		for i, j := 0, len(row)-1; i < j; i, j = i+1, j-1 {
			row[i], row[j] = 1^row[j], 1^row[i]
		}
		if n%2 != 0 {
			row[int(n/2)] ^= 1
		}
	}
	return A
}

func main() {
	A := [][]int{{0, 1, 1}, {1, 0, 1}, {0, 1, 0}}
	fmt.Println(flipAndInvertImage(A))
}
