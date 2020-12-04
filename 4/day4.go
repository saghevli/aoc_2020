package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strings"
)

func ReadLinesStr(fileName string) (passports []string) {
	fileBytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		os.Exit(1)
	}
	for _, pass := range strings.Split(string(fileBytes), "\n\n") {
		passports = append(passports, strings.Split(
			strings.Replace(pass, "\n", " ", -1), " ")...)
		passports = append(passports, "EOL")
	}
	for _, p := range passports {
		fmt.Println(p)
	}
	return passports
}

func getNumValidStrs(passports []string) (count int) {
	patterns := []string{
		"^byr:(19[2-9][0-9]|200[0-2])$",
		"^iyr:(201[0-9]|2020)$",
		"^eyr:(202[0-9]|2030)$",
		"^hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$",
		"^hcl:#[0-9a-f]{6}$",
		"^ecl:(amb|blu|brn|gry|grn|hzl|oth)$",
		"^pid:[0-9]{9}$"}
	// "^cid:.*$"}
	passCount := [7]int{0, 0, 0, 0, 0, 0, 0}
	for _, pass := range passports {
		if pass == "EOL" {
			fmt.Println(passCount)
			if passCount == [7]int{1, 1, 1, 1, 1, 1, 1} {
				count++
			}
			passCount = [7]int{0, 0, 0, 0, 0, 0, 0}
			continue
		}
		for i, pat := range patterns {
			if len(pass) > 3 && pat[1:4] == pass[0:3] {
				fmt.Println("pass: " + pass)
				fmt.Println("pat: " + pat)
			}
			if match, _ := regexp.MatchString(pat, pass); match {
				fmt.Println("*MATCH*")
				passCount[i]++
				break
			}
		}
	}
	return count
}

func main() {
	data1 := ReadLinesStr(os.Args[1])
	tot1 := getNumValidStrs(data1)
	fmt.Println(tot1)
}
