# Assignment 4 - Exercise 2
# Name: Your name here
# Student ID: Your ID here

# Assign the $search_directory variable from the first command line argument

# * * * YOU PUT CODE HERE * * * 

# Print a sentence that tells the user what the script is doing
Write-Output "Searching all .txt files in $search_directory for email addresses..."

# Combine the directory path and the wildcard filter to search only in .txt files
$files_to_search = Join-Path $search_directory "*.csv"

# Search all .txt files in the specified directory for valid email addresses

# THE VARIABLE IS WRONG - CHANGE IT TO THE RIGHT NAME PER THE ASSIGNMENT INSTRUCTIONS
$email_SWOR = Select-String -Path $files_to_search -Pattern "EMAIL_REGEX_GOES_HERE"
$email_count = ($email_SWOR | Measure-Object).count
Write-Output $email_SWOR
Write-Output "$email_count emails were found." 

# YOU CAN TEST THIS BY RUNNING LIKE THIS:
# ./A4E1.ps1 "C:\YOUR\PATH\TO\DATA_FILES_FROM_ZIP\"
