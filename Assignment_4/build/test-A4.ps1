function New-TestCase {
    param (
        [Parameter(Mandatory=$true)][string]$Name,
        [Parameter(Mandatory=$true)][string]$Output,
        [double]$Score,
        [double]$MaxScore,
        [string]$Visibility,
        [string]$Status,
        [string]$OutputFormat,
        [string]$Number,
        [string[]]$Tags,
        [hashtable]$ExtraData
    )

    $testCase = @{
        name       = $Name
        output     = $Output
        score      = $Score
    }

    if ($MaxScore) { $testCase["max_score"] = $MaxScore }
    if ($Status) { $testCase["status"] = $Status }
    if ($Visibility) { $testCase["visibility"] = $Visibility }
    if ($Number) { $testCase["number"] = $Number }
    if ($Tags) { $testCase["tags"] = $Tags }
    if ($ExtraData) { $testCase["extra_data"] = $ExtraData }
    if ($OutputFormat) { $testCase["output_format"] = $OutputFormat }


    return $testCase
}

function WriteAndSaveTest {
    param (
        $results,
        $testsArray
    )

    # Calculate the total score from the test cases
    $totalScore = ($testsArray | Measure-Object -Property score -Sum).Sum
    # If the total score is negative, adjust it to 0
    if ($totalScore -lt 0) {
        foreach ($test in $testsArray) {
            $test.score = 0
        }
    }
    
    $results.tests = $testsArray

    $jsonData = $results | ConvertTo-Json -Depth 4
    $jsonData | Out-File -Path "/autograder/results/results.json" -Encoding utf8 -Force

    return $results
}

$testsArray = @()

$results = @{
    output             = "Thank you for your submission."
    output_format      = "simple_format"
    test_output_format = "md"
    test_name_format   = "simple_format"
    visibility         = "visible"
    stdout_visibility  = "visible"
    extra_data         = @{}
}

$submissionFolder = "/autograder/submission/A4*.ps1"
$submission = get-childitem $submissionFolder

Write-Output "Validating submission..."
if($null -eq $submission) {
    Write-Verbose "No submission found."
    $testsArray += New-TestCase -Name "Marks for submitting a file" -Output "Your submission did not include a powershell script. This means it cannot be graded and results in a grade of 0." -Score -50.0 -Status 'failed'
    return WriteAndSaveTest -results $results -testsArray $testsArray
}

Write-Output "Validating file count..."
if(($submission | Measure-Object).count -eq 2) {
    Write-Verbose "Two files detected."
    $testsArray += New-TestCase -Name "Marks for counting to two" -Output "Correct number of files submitted" -Status 'passed' -score 10.0
} else {
    Write-Verbose "!2 files detected."
    $testsArray += New-TestCase -Name "Marks for counting to two" -Output "Incorrect amount of files submitted" -Status 'fail'
}

Write-Output "Checking filename..."
if(($submission[0].Name -like "A4E1.ps1") -and ($submission[1].Name -like "A4E2.ps1")) {
    Write-Verbose "Filenames correct."
    $testsArray += New-TestCase -Name "A4E1: Filename" -Output "Your submission contains the correct filename" -Status 'passed' -score 5.0
} else {
    Write-Verbose "Incorrect filenames detected."
    $testsArray += New-TestCase -Name "A4E1: Filename" -Output "Your submission contains the incorrect filename" -Status 'failed'
}

Write-Output "Executing script..."
try {
    $testLaunch = . /autograder/submission/A4E1.ps1 "$PSScriptroot/data/"
    #Write-Output $testLaunch
    Write-Verbose "Script executed without errors."
    $testsArray += New-TestCase -Name "A4E1: Does it run?" -Output "Your submission executed without errors" -Status 'passed' -score 20.0
} catch {
    Write-Verbose "Error detected during script execution."
    $testsArray += New-TestCase -Name "A4E1: Does it run?" -Output "Your submission did not successfully execute without errors. This means it cannot be graded and results in a grade of 0." -Score -50.0 -Status 'failed'
    return WriteAndSaveTest -results $results -testsArray $testsArray
}

Write-Output "Validating variables..."
if($null -eq $search_directory) {
    Write-Verbose "No Search Directory variable detected."
    $testsArray += New-TestCase -Name "A4E1: Checking search_directory variable" -Output "No Search Directory variable detected" -Visibility "visible" -status 'failed'
} else {
    Write-Verbose "Search Directory variable detected."
    $testsArray += New-TestCase -Name "A4E1: Checking search_directory variable" -Output "Correct Search Directory variable detected" -Visibility "visible" -status 'passed' -score 5.0
}

if($null -eq $email_rows) {
    Write-Verbose "No email_rows variable detected."
    $testsArray += New-TestCase -Name "A4E1: Checking email_rows variable" -Output "No email_rows variable detected" -Visibility "visible" -status 'failed'
} else {
    Write-Verbose "email_rows variable detected."
    $testsArray += New-TestCase -Name "A4E1: Checking email_rows variable" -Output "Correct email_rows variable detected" -Visibility "visible" -status 'passed' -score 5.0
}

Write-Output "Comparing script output with expected result..."
$expectedresult = . $PSScriptroot/Find-EmailSolution.ps1 "/autograder/source/data/"
# Format objects to string literals
$expectedresult = $expectedresult | ForEach-Object {$_.ToString()} | select-Object -first 3 -last 3
$testLaunchString = $testLaunch | ForEach-Object {$_.ToString()} | select-Object -first 3 -last 3
$OutputCompare = Compare-Object -ReferenceObject $expectedresult -DifferenceObject $testLaunchString
if( -not $OutputCompare
) {
    Write-Verbose "Output is identical or close enough to fool the test cases"
    $testsArray += New-TestCase -Name "A4E1: Script Output" -Output "Your output matched the test cases exactly or at least close enough to trick them.  Great work." -Visibility "visible" -status 'passed' -score 5.0

} else {
    #Finding Differences
    $WrongLines = $outputCompare | ForEach-Object {if($_.sideIndicator -like '=>'){$_.InputObject}}
    Write-Verbose "Output does not match expected result."
    $testsArray += New-TestCase -Name "A4E1: Script Output" -Output @"
    Output that does not match:
    * * * * * * *
    $wrongLines
    * * * * * * *
    Expected Output: 
    * * * * * * *
    $expectedresult
    * * * * * * *


"@ -Visibility "visible" -status 'failed'
}

# Define the expected output for verification
$expectedOutput = @(
    "Exercise 1 - 15 Matches found!",
    "Exercise 2 - 1 Matches found!",
    "Exercise 3 - 63 Matches found!",
    "Exercise 4 - 5 Matches found!",
    "Exercise 5 - 7 Matches found!",
    "Exercise 6 - 16 Matches found!",
    "Exercise 7 - 1 Matches found!",
    "Exercise 8 - 2 Matches found!"
)

# Verify script output
$scriptPath = '/autograder/submission/A4E2.ps1'
$scriptOutput = . /autograder/submission/A4E2.ps1
$match = Compare-Object -ReferenceObject $expectedOutput -DifferenceObject $scriptOutput -SyncWindow 0
$mismatch = ($match  | Where-Object {$_.SideIndicator -eq '<='}).InputObject
Write-Output $mismatch
if ($null -eq $match) {
    $testsArray += New-TestCase -Name "A4E2: Verify Script Output" -Output "Script output matches expected." -Score 25 -MaxScore 25 -Status "passed"
} else {
    $testsArray += New-TestCase -Name "A4E2: Verify Script Output" -Output "Script output does not match expected.`nDifference:`n$mismatch" -Score 0 -MaxScore 25 -Status "failed"
}





# Check source code for compliance
$scriptContent = Get-Content -Path $scriptPath | Where-Object { $_.Trim() -and $_ -notmatch '^\s*#' } | Select-Object -Last 10
$nonCompliantLines = $scriptContent | Where-Object { $_ -notmatch '^\s*\$|^\s*Test-Regex' }

if ($nonCompliantLines.Count -eq 0) {
    $testsArray += New-TestCase -Name "A4E2: Source Code Inspection" -Output "Source code inspection passed." -Score 25 -MaxScore 25 -Status "passed"
} else {
    $testsArray += New-TestCase -Name "A4E2: Source Code Inspection" -Output "Source code contains non-compliant lines.  Did you just try to beat the system by writing out the number instead of doing the Regex?  NAUGHTY!  These lines look bad:`n$nonCompliantLines" -Score 0 -MaxScore 25 -Status "failed"
}


return WriteAndSaveTest -results $results -testsArray $testsArray
