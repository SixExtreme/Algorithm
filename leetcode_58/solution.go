package main

import "fmt"

//func lengthOfLastWord(s string) int {
//	if s == "" {
//		return 0
//	}
//
//	j := len(s) - 1
//	for j > -1 {
//		if s[j] != ' ' {
//			break
//		} else {
//			j--
//		}
//	}
//
//	i := j
//	for i > -1 {
//		if s[i] == ' ' {
//			break
//		} else {
//			i--
//		}
//	}
//
//	return j - i
//}

func lengthOfLastWord(s string) int {
	if s == "" {
		return 0
	}

	j := len(s) - 1
	for j > -1 && s[j] == ' ' {
		j--
	}

	l := 0
	for j > -1 && s[j] != ' ' {
		l++
		j--
	}

	return l
}

func main() {
	s := "  a "
	fmt.Println(lengthOfLastWord(s))
}