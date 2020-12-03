package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

type Pair struct {
	low, high int
}

func ReadLines(r io.Reader) (grid []string) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanLines)
	i := 0
	for scanner.Scan() {
		line := scanner.Text()
		grid = append(grid, line)
		i++
	}
	return grid
}

func getNumTrees(grid []string, horizJump, vertJump int) (count int) {
	var j int = horizJump
	var rowLen = len(grid[0])
	for i := vertJump; i < len(grid); i = i + vertJump {
		if i == len(grid) {
			break
		}
		if grid[i][j] == '#' {
			count = count + 1
		}
		j = (j + horizJump) % rowLen
	}
	return count
}

func main() {
	r, _ := os.Open(os.Args[1])
	grid := ReadLines(r)
	tot := getNumTrees(grid, 1, 1) *
		getNumTrees(grid, 3, 1) *
		getNumTrees(grid, 5, 1) *
		getNumTrees(grid, 7, 1) *
		getNumTrees(grid, 1, 2)
	fmt.Println(tot)
}
