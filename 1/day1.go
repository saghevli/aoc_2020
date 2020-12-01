package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
)

func ReadInts(r io.Reader) (result []int, e error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return result, err
		}
		result = append(result, x)
	}
	return result, scanner.Err()
}

// brute force triple nested loop
// optimize by sorting:
// for two ints, n*logn (iterate + search for matching value)
// for three ints...n^2 logn is straightforward. how to faster?
func SumsTo2020ThreeBrute(expenses []int) (total int) {
	found := false
	var s, s2, s3 int
	for _, e := range expenses {
		for _, e2 := range expenses {
			for _, e3 := range expenses {
				if e+e2+e3 == 2020 {
					s = e
					s2 = e2
					s3 = e3
					break
				}
			}
			if found {
				break
			}
		}
		if found {
			break
		}
	}
	return s * s2 * s3
}

// brute force double nested loop
func SumsTo2020TwoBrute(expenses []int) (total int) {
	found := false
	var s, s2 int
	for _, e := range expenses {
		for _, e2 := range expenses {
			if e+e2 == 2020 {
				s = e
				s2 = e2
				break
			}
		}
		if found {
			break
		}
	}
	return s * s2
}

// finds two ints summing to 2020 and returns their product, using binary search
func SumsTo2020FastTwo(expenses []int) (total int) {
	sort.Ints(expenses)
	for _, e := range expenses {
		index := sort.Search(len(expenses), func(i int) bool {
			return expenses[i] >= 2020-e
		})
		if index < len(expenses) && expenses[index] == 2020-e {
			return e * expenses[index]
		}
	}
	return -1
}

func main() {
	r, _ := os.Open(os.Args[1])
	expenses, _ := ReadInts(r)
	fmt.Printf("double sum binary: %d\n", SumsTo2020FastTwo(expenses))
	fmt.Printf("double sum brute: %d\n", SumsTo2020TwoBrute(expenses))
	fmt.Printf("triple sum brute: %d\n", SumsTo2020ThreeBrute(expenses))
}
