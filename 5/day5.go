package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

type Pair struct {
	row, col int
}

func ReadLinesStr(fileName string) (plane []string) {
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		os.Exit(1)
	}
	plane = strings.Split(string(fileBytes), "\n")
	return plane
}

func getNumValidStrs(plane []string) (max int) {
	var seatList []Pair
	// for funsies, make and init a seatmap
	var seatMap [127][8]string
	for i, row := range seatMap {
		for j, _ := range row {
			seatMap[i][j] = "."
		}
	}
	// iterate and discover seat assignments, populate seatlist
	for _, row := range plane {
		var low, high int = 0, 127
		var left, right int = 0, 7
		for i, half := range row {
			if i < 7 {
				if half == 'F' {
					high = low + (high-low)/2
				} else if half == 'B' {
					low = low + (high-low)/2 + 1
				}
			} else {
				if half == 'L' {
					right = left + (right-left)/2
				} else if half == 'R' {
					left = left + (right-left)/2 + 1
				}
			}
		}
		seatId := 8*low + left
		seatList = append(seatList, Pair{low, left})
		if max < seatId {
			max = seatId
		}
	}
	var rows [127]int
	var cols [8]int
	// fill row/column counts + seatMap
	for _, seat := range seatList {
		rows[seat.row]++
		cols[seat.col]++
		seatMap[seat.row][seat.col] = "X"
	}
	for _, row := range seatMap {
		for _, col := range row {
			fmt.Print(col)
		}
		fmt.Print("\n")
	}
	// find seat by locating row with 7 seats and col with fewest seats
	// slightly ambiguous: what do if the missing seat is in a col with
	// an extra seat and there is a tie?
	mySeat := Pair{-1, -1}
	var m int = 8
	for i, row := range rows {
		if row == 7 {
			m = row
			mySeat.row = i
		}
	}
	m = 127
	for i, col := range cols {
		if m > col {
			m = col
			mySeat.col = i
		}
	}
	fmt.Println(mySeat)
	return 8*mySeat.row + mySeat.col

}

func main() {
	data := ReadLinesStr(os.Args[1])
	tot := getNumValidStrs(data)
	fmt.Println(tot)
}
