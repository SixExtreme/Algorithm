package main

import "fmt"

func generate(numRows int) [][]int {
	tri := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		lenRow := i + 1
		tri[i] = make([]int, lenRow)
		tri[i][0], tri[i][lenRow - 1] = 1, 1
		for j := 1; j < lenRow - 1; j++ {
			tri[i][j] = tri[i-1][j] + tri[i - 1][j - 1]
		}
	}
	return tri
}

func main() {
	numRows := 5
	fmt.Println(generate(numRows))
}
