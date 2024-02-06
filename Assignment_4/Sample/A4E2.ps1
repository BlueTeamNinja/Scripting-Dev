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
    param( [string]$regex, [string]$string, [int]$exercise )
    if ($string -match $regex) {
        $x = $string | Select-String -Pattern $regex -AllMatches
        $count = $x.Matches.Count
        "Exercise $exercise - $count Matches found!"
    } else {
        "Exercise $exercise - No match found for $regex"
    }
}


# Exercise 1 
$regex1 = '[aA]'
Test-Regex -regex $regex1 -string $testString -exercise 1

# Exercise 2
$regex2 = '86'
Test-Regex -regex $regex2 -string $testString -exercise 2

# Exercise 3
$regex3 = '[aeiou]'
Test-Regex -regex $regex3 -string $testString -exercise 3

# Exercise 4
$regex4 = '(?ms)^[A-z]'
Test-Regex -regex $regex4 -string $testString -exercise 4

# Exercise 5
$regex5 = '\b\w{5}\b'
Test-Regex -regex $regex5 -string $testString -exercise 5

# Exercise 6
$regex6 = '\d'
Test-Regex -regex $regex6 -string $testString -exercise 6

# Testing Exercise 7 - Match All Numbers
$regex7 = '\d{4}-\d{2}-\d{2}'
Test-Regex -regex $regex7 -string $testString -exercise 7

# Testing Exercise 8 - Match Hexadecimal Colors
$regex8 = '#[0-9A-Fa-f]{6}'
Test-Regex -regex $regex8 -string $testString -exercise 8