package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	fileBytes, _ := ioutil.ReadFile(os.Args[1])
	qArr := strings.Split(string(fileBytes), "\n\n")
	counts := [26]int{}
	var countLetters int
	// iterate over groups
	for _, qP := range qArr {
		// number of people in group
		var numPeople = strings.Count(qP, "\n") + 1
		// for each question, fill counts at the index of the letter
		for _, q := range qP {
			if q != '\n' {
				counts[rune(q)-'a']++
			}
		}
		// for each group, find:
		// p1:questions that anyone answered yes to
		// p2:questions that everyone answered yes to
		for _, count := range counts {
			// if count > 0 { // part 1
			if count == numPeople { // part 2
				countLetters++
			}
		}
		// reset counts for next group
		counts = [26]int{}
	}
	fmt.Println(countLetters)
}
