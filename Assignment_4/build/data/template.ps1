# Assignment 4 - Exercise 2
# Name: Your name here
# Student ID: Your ID here

# This powershell script solves world hunger through basic regular expression exercises

$testString = @"
It is a shiny day in 2024-02-06 in COMP86,  
where code becomes art and pixels dance,  
even computers can't help but admire his tricks,  
Abe teaches not just with logic but with great pants.  
The colours #FFEE09 and #5522AA don't rhyme with anything.  
"@

# Function to test regex
function Test-Regex {
    param(
        [string]$regex,
        [string]$string, 
        [int]$exercise
    )

    if ($string -match $regex) {
        "Exercise $exercise - $($Matches.Count) Matches found: $($Matches.Values)"
    } else {
        "Exercise $exercise - No match found for $regex."
    }
}


# Testing Exercise 1
$regex1 = "[aA]"
Test-Regex -regex $regex1 -string $testString -exercise 1

# Testing Exercise 2
$regex2 = ""
Test-Regex -regex $regex2 -string $testString -exercise 2

# Testing Exercise 3
$regex3 = ""
Test-Regex -regex $regex3 -string $testString -exercise 3

# Testing Exercise 4
$regex4 = ""
Test-Regex -regex $regex4 -string $testString -exercise 4

# Testing Exercise 5
$regex5 = ""
Test-Regex -regex $regex5 -string $testString -exercise 5

# Testing Exercise 6
$regex6 = ""
Test-Regex -regex $regex6 -string $testString -exercise 6

# Testing Exercise 7
$regex7 = ""
Test-Regex -regex $regex7 -string $testString -exercise 7

# Testing Exercise 8
$regex8 = ""
Test-Regex -regex $regex8 -string $testString -exercise 8
