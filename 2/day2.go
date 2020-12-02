package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Pair struct {
	low, high int
}

func ReadLines(r io.Reader) (counts []Pair, letters []string, pwds []string) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	re, _ := regexp.Compile("([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+$)")
	i := 0
	for scanner.Scan() {
		line := scanner.Text()
		matches := re.FindStringSubmatchIndex(line)
		low, _ := strconv.Atoi(line[matches[2]:matches[3]])
		high, _ := strconv.Atoi(line[matches[4]:matches[5]])
		counts = append(counts, Pair{low, high})
		letters = append(letters, line[matches[6]:matches[7]])
		pwds = append(pwds, line[matches[8]:matches[9]])
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
	fmt.Println(countLegalPwds1(counts, letters, pwds))
	fmt.Println(countLegalPwds2(counts, letters, pwds))
}
