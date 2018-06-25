package main

import "fmt"

func judgeCircle(moves string) bool {
	x, y := 0, 0
	for _, step := range moves {
		switch string(step) {
		case "L":
			x -= 1
		case "R":
			x += 1
		case "U":
			y += 1
		case "D":
			y -= 1
		}
	}
	return (x == 0) && (y == 0)
}

func main() {
	moves := "UDDD"
	ret := judgeCircle(moves)
	fmt.Println(ret)
}
