# Assignment 3

You are about to create your first script as an assignment.  I'm also using an autograder for the first time for this, so let's all learn together.  If something comes up weird, I'll gladly fix it for you. 

## Requirements

1. Your script named `A3E1.ps1`
1. Your CSV file named `organizations-1000.csv` which is available on D2L under Module 3. 

Do *NOT* use any other names.  These are exactly what the autograder is looking for and if you get the names wrong, it won't run and I have nothing to mark. 

## Assignment

1. Create a variable named `$results` containing the CSV data from `.\organizations-1000.csv`
1. Create a variable named `$query` containing the FIRST typed argument after your script is ran. 
1. Create a variable named `$output` containing the output of `$results` where the `Industry` property is like the `$query` variable.
1. Display the $output variable without any formatting.  **Do not** use `Write-Host` or `echo`.  

## Rules
* Do not use any other variable names or you will lose points.
* Do not use `Write-Host` to display output, it is very different from `Write-Output` especially in scripts.  
* I have created test cases with a variety of values of query that must match, so do not edit the source data and do not add any additional characters to the value of query.  E.g.  Do not assume a `*` character, test by using it as the argument.  
* Test your script before uploading!  It must run without errors and one of the test cases I use is: `./A3E1.ps1 Computer*` and I am expecting 32 results. 