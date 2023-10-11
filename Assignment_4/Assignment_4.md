# Assignment 4 

Create a powershell script that: 

1. Accepts a filepath as an argument and stores it in the variable `$search_directory`
1. Search all CSV files in the given path for email addresses and stores it in the variable `$email_rows`.
1. Count the number of email objects and store it as email_count
1. Displays exactly this output with the variables displaying the proper values: 
``
Searching all .txt files in $search_directory for email addresses...
$email_rows
$email_count emails were found.
```


1. Also Display: 
> There are `N` email addresses in the path `PATH`

## Submission

Upload only `assignment_4.ps1` to the autograder. 
You do not need to upload any csv files, ones will be generated similar (but not identical) to the ones on D2L.

## Important Notes and Requirements

* Ensure your text is exactly as shown above where N is the number of email addresses and PATH is the path entered as an argument (in other words, its the value of `$search_directory`). 

* Use the regular expression for matching emails from the PDF.  Do NOT use one from the internet as the results will vary slightly and your results must match exactly to the ones that match from that 

* Ensure you use either `Join-Path` or `Get-ChildItem` on the user input before searching.  To verify this, test your script by entering a path both with and without a trailing slash, as an example (that will not work on your computer, its just an example): `D:\Code\Samples` AND `D:\Code\Samples\`.  Using `Join-Path` or `Get-ChildItem` will solve this trailing slash problem for you with the `$search_directory` variable.

* For extra challenge, you may also attempt to accept a **named parameter** with a default value instead of using the special argument variable.