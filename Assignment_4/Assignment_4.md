# Assignment 4 

Create a powershell script that: 

1. Accepts a filepath as an argument and stores it in the variable `$search_directory`
1. Search all CSV files in the given path for email addresses and stores it in the variable `$email_rows`.  Use the csv files in `assignment4_data.zip`.
1. Count the number of email objects and store it as email_count.  
1. Displays the sample output with the variables displaying their proper values.

How to count the emails:
```
$email_count = ($email_rows | Measure-Object).count
```

Expected display format:
```
Searching all .txt files in $search_directory for email addresses...
$email_rows
$email_count emails were found.
```

## Submission

Upload only `assignment_4.ps1` to the autograder. 
You do not need to upload any csv files, ones will be generated similar (but not identical) to the ones on D2L.

## Important Notes and Requirements

* Ensure your text is exactly as shown above where N is the number of email addresses and PATH is the path entered as an argument (in other words, its the value of `$search_directory`). 

* Use the regular expression for matching emails from the PDF.  Do NOT use one from the internet as the results will vary slightly and your results must match exactly to the ones that match from that 

* Ensure you use either `Join-Path` or `Get-ChildItem` on the user input before searching.  To verify this, test your script by entering a path both with and without a trailing slash, as an example (that will not work on your computer, its just an example): `D:\Code\Samples` AND `D:\Code\Samples\`.  Using `Join-Path` or `Get-ChildItem` will solve this trailing slash problem for you with the `$search_directory` variable.

* For extra challenge, you may also attempt to accept a **named parameter** with a default value instead of using the special argument variable.

For demonstration, your output should look like this, but with different paths and a different number of emails but in this format when your script is complete:
```
PS D:\Code\Sample> .\Find-Emails.ps1 ..\Data\
Searching all .txt files in ..\Data\ for email addresses...

D:\Code\Data\output_1.csv:2:"Franklin","Mason","Hockey","email","masonfranklin@hotmail.com"
D:\Code\Data\output_1.csv:3:"Brian","Dean","Volleyball","email","brian.dean@netnavigators.org"
D:\Code\Data\output_1.csv:4:"Piper","Wood","Tennis","email","silverlion365@hotmail.com"
D:\Code\Data\output_1.csv:5:"Peter","Fields","Hockey","email","greenfrog642@webwarden.org"
D:\Code\Data\output_1.csv:6:"Jessie","Steward","Tennis","email","smallladybug723@netcrafters.org"
D:\Code\Data\output_1.csv:9:"Lucas","Hughes","Tennis","email","lucas_hughes@globalgrid.biz"
D:\Code\Data\output_1.csv:13:"Bertha","Mckinney","Golf","email","mckinney.bertha@business.net"
D:\Code\Data\output_1.csv:14:"Patsy","Palmer","Golf","email","palmerpatsy@globaldataflow.net"
D:\Code\Data\output_1.csv:16:"Oliver","Pelletier","Rugby","email","pelletier.oliver@quantumcode.net"
D:\Code\Data\output_1.csv:17:"Adrian","Webb","Soccer","email","webb.adrian@netnavigator.com"
10 emails were found.

PS D:\Code\Sample>
```

