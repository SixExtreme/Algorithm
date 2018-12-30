package main

import "fmt"

//func twoSum(numbers []int, target int) []int {
//	m := make(map[int]int, len(numbers))
//	for j, x := range numbers {
//		i, has := m[x]
//		if has {
//			return []int{i + 1, j + 1}
//		} else {
//			m[target - x] = j
//		}
//	}
//	return []int{-1, -1}
//}

func twoSum(numbers []int, target int) []int {
	i, j := 0, len(numbers) - 1
	for {
		sum := numbers[i] + numbers[j]
		if sum == target {
			return []int{i + 1, j + 1}
		} else if sum < target {
			i += 1
		} else {
			j -= 1
		}
	}
}

func main() {
	numbers := []int{2, 7, 11, 15}
	fmt.Println(twoSum(numbers, 9))
}