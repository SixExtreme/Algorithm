package main

import (
	"fmt"
)

func isValid(s string) bool {
	var stack []byte
	for _, c := range s {
		if c == '(' {
			stack = append(stack, ')')
		} else if c == '[' {
			stack = append(stack, ']')
		} else if c == '{' {
			stack = append(stack, '}')
		} else if len(stack) == 0 {
			return false
		} else {
			peek := stack[len(stack) - 1]
			stack = stack[:(len(stack) - 1)]
			if peek != byte(c) {
				return false
			}
		}
	}
	return len(stack) == 0
}

func main()  {
	fmt.Println(isValid("{[]}"))
}

