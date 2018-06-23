package main

import (
	"fmt"
)

func uniqueMorseRepresentations(words []string) int {
	codes := []string{
		".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", 
		"-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	mapset := make(map[string]bool)
	for _, word := range words {
		var buf string
		for _, c := range(word) {
			buf += codes[c - 'a']
		}
		mapset[buf] = true
	}
	return len(mapset)
}

func main () {
	words := []string{"gin", "zen", "gig", "msg"}
	ret := uniqueMorseRepresentations(words)
	fmt.Println(ret)
}