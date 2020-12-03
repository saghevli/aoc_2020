package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

type Pair struct {
	low, high int
}

func ReadLines(fileName string) (grid []string) {
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	return strings.Split(string(fileBytes), "\n")
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
	grid := ReadLines(os.Args[1])
	tot := getNumTrees(grid, 1, 1) *
		getNumTrees(grid, 3, 1) *
		getNumTrees(grid, 5, 1) *
		getNumTrees(grid, 7, 1) *
		getNumTrees(grid, 1, 2)
	fmt.Println(tot)
}
