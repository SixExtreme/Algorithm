package main

import "fmt"

func lengthOfLastWord(s string) int {
	if s == "" {
		return 0
	}

	j := len(s) - 1
	for j > -1 {
		if s[j] != ' ' {
			break
		} else {
			j--
		}
	}

	i := j
	for i > -1 {
		if s[i] == ' ' {
			break
		} else {
			i--
		}
	}

	return j - i
}

func main() {
	s := "  a "
	fmt.Println(lengthOfLastWord(s))
}