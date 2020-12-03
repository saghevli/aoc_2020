package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

type Pair struct {
	low, high int
}

func ReadLines(r io.Reader) (counts []Pair, letters []string, pwds []string) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	i := 0
	for scanner.Scan() {
		var low, high int
		var letter rune
		var pwd string
		fmt.Sscanf(scanner.Text(), "%d-%d %c: %s", &low, &high, &letter, &pwd)
		counts = append(counts, Pair{low, high})
		letters = append(letters, string(letter))
		pwds = append(pwds, pwd)
		i++
	}
	return counts, letters, pwds
}

func countLegalPwds1(counts []Pair, letters []string, pwds []string) (count int) {
	for i, _ := range counts {
		numOccurrences := strings.Count(pwds[i], letters[i])
		if numOccurrences >= counts[i].low && numOccurrences <= counts[i].high {
			count = count + 1
		}
	}
	return count
}

func countLegalPwds2(counts []Pair, letters []string, pwds []string) (count int) {
	for i, _ := range counts {
		matches := 0
		if string(pwds[i][counts[i].low-1]) == letters[i] {
			matches = matches + 1
		}
		if string(pwds[i][counts[i].high-1]) == letters[i] {
			matches = matches + 1
		}
		if matches == 1 {
			count = count + 1
		}
	}
	return count
}

func main() {
	r, _ := os.Open(os.Args[1])
	counts, letters, pwds := ReadLines(r)
	fmt.Printf("%v", counts)
	fmt.Printf("%v", letters)
	fmt.Printf("%v", pwds)
	fmt.Println(countLegalPwds1(counts, letters, pwds))
	fmt.Println(countLegalPwds2(counts, letters, pwds))
}
