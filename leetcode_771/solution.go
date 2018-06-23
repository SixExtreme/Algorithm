package main

import (
	"fmt"
	"strings"
)

func numJewelsInStones(J string, S string) int {
	sum := 0
	for _, j := range J {
		sum += strings.Count(S, string(j))
	}
	return sum;
}

func main()  {
	J := "aA"
	S := "aAAbbbb"
	ret := numJewelsInStones(J, S)
	fmt.Println(ret)
}