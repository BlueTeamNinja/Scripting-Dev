# Assignment 1
## Scripting Introduction

# Instructions

For this exercises, create a Powershell scripts as described in the exercise instructions. Save this script in a separate files named A1En.ps1, where n is the exercise number. For exercise 1 this means your file name would be `A1E1.ps1`. Submit this script file to Gradescope Assignment 1.

The hardest script you'll ever make is the first one!  Everyone started somewhere and you're about to begin a great journey. 


# Exercise 1

We are going to make a powershell script that simply displays some stuff to the screen. Exercise requirements are always in bullet point lists like this. 

 - Create a script that says exactly: `My name is [Your Name] and I am going to ROCK this course!`
 - The phrase is case sensitive
 - You must replace `[Your name]` with your name (or any word other than my name)

This is the expected output:
```
PS C:\Users\Abe\Code> A1E1.ps1
My name is Abe and I am going to ROCK this course!
```

In order to do this, I am going to give you all the code.  Copy and paste everything below into a new text file (Try using Visual Studio Code) and save it as `A1E1.ps1` anywhere on your hard drive, but remember which folder you saved it in! 

```
# This is your first script
# These are comments, they don't actually do anything in the code.  
# All of this will make more sense as we go through the course!

$name = "Abe"

Write-Output "My name is $name and I am going to ROCK this course!"

# Copy and paste all of this into a file and 
# save it as A1E1.ps1

# We will then upload it to Gradescope to see how we did!
```

Excellent.  You are going to do great! 