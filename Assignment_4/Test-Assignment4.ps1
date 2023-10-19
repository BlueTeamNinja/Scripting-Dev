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

    return $testCase
}

function WriteAndSaveTest {
    param (
        $results,
        $testsArray
    )

    $results.tests = $testsArray

    $jsonData = $results | ConvertTo-Json -Depth 4
    $jsonData | Out-File -Path "/autograder/results/results.json" -Encoding utf8 -Force

    return $results
}

$testsArray = @()

$results = @{
    output             = "Thank you for your submission."
    output_format      = "simple_format"
    test_output_format = "simple_format"
    test_name_format   = "simple_format"
    visibility         = "visible"
    stdout_visibility  = "visible"
    extra_data         = @{}
}

$submissionFolder = "/autograder/submission/*.ps1"
$submission = get-childitem $submissionFolder

Write-Output "Validating submission..."
if($null -eq $submission) {
    Write-Verbose "No submission found."
    $testsArray += New-TestCase -Name "**FAIL** - No submission" -Output "Your submission did not include a powershell script. This means it cannot be graded and results in a grade of 0." -Score -50.0 -Status 'failed'
    return WriteAndSaveTest -results $results -testsArray $testsArray
}

Write-Output "Validating file count..."
if(($submission | Measure-Object).count -gt 1) {
    Write-Verbose "Multiple files detected."
    $testsArray += New-TestCase -Name "Count submissions" -Output "Too many files submitted" -Status 'failed'
} else {
    Write-Verbose "Single file detected."
    $testsArray += New-TestCase -Name "Count submissions" -Output "Correct amount of files submitted" -Status 'passed' -score 5.0
}

Write-Output "Checking filename..."
if($submission[0].Name -like "assignment_4.ps1") {
    Write-Verbose "Filename is correct."
    $testsArray += New-TestCase -Name "Correct Filename" -Output "Your submission contains the correct filename" -Status 'passed' -score 5.0
} else {
    Write-Verbose "Incorrect filename detected."
    $testsArray += New-TestCase -Name "Incorrect Filename" -Output "Your submission contains the incorrect filename" -Status 'failed'
}

Write-Output "Executing script..."
try {
    $testLaunch = . $submission[0].FullName "$PSScriptroot/data/"
    Write-Output $testLaunch
    Write-Verbose "Script executed without errors."
    $testsArray += New-TestCase -Name "Script Execution" -Output "Your submission executed without errors" -Status 'passed' -score 20.0
} catch {
    Write-Verbose "Error detected during script execution."
    $testsArray += New-TestCase -Name "**FAIL** - Script Execution" -Output "Your submission did not successfully execute without errors. This means it cannot be graded and results in a grade of 0." -Score -50.0 -Status 'failed'
    return WriteAndSaveTest -results $results -testsArray $testsArray
}

Write-Output "Testing for trailing slash..."
$testLaunch_notrail = . $submission[0].FullName "$PSScriptroot/data"
if(Compare-Object -ReferenceObject $testLaunch.toString() -DifferenceObject $testLaunch_notrail.toString()) {
    Write-Verbose "Different results detected with/without trailing slash."
    $testsArray += New-TestCase -Name "Trailing slash test" -Output @"
    Your submission produces different results with or without a trailing slash.
    output without a trailing slash: 
    ``````
    $testLaunch_notrail
    ``````
    output with a trailing slash:
    ``````
    $testLaunch
    ``````
"@ -Status 'failed' -OutputFormat 'md'
} else {
    Write-Verbose "Identical results with/without trailing slash."
    $testsArray += New-TestCase -Name "Trailing slash test" -Output "Your submission produces identical results with or without a trailing slash." -Status 'passed' -score 5.0
}

Write-Output "Validating variables..."
if($null -eq $search_directory) {
    Write-Verbose "No Search Directory variable detected."
    $testsArray += New-TestCase -Name "Search Directory" -Output "No Search Directory variable detected" -Visibility "visible" -status 'failed'
} else {
    Write-Verbose "Search Directory variable detected."
    $testsArray += New-TestCase -Name "Search Directory" -Output "Correct Search Directory variable detected" -Visibility "visible" -status 'passed' -score 5.0
}

if($null -eq $email_rows) {
    Write-Verbose "No email_rows variable detected."
    $testsArray += New-TestCase -Name "Email Rows" -Output "No email_rows variable detected" -Visibility "visible" -status 'failed'
} else {
    Write-Verbose "email_rows variable detected."
    $testsArray += New-TestCase -Name "Email Rows" -Output "Correct email_rows variable detected" -Visibility "visible" -status 'passed' -score 5.0
}

Write-Output "Comparing script output with expected result..."
$expectedresult = . $PSScriptroot/Find-EmailSolution.ps1 "$PSScriptroot/data/"
if(
        $expectedresult[$expectedresult.length-1] -eq $testLaunch[$testLaunch.length-1] -and
        $expectedresult[0] -eq $testLaunch[0] -and
        $expectedresult[1] -eq $testLaunch[1] -and
        $expectedresult.length -eq $testLaunch.length
) {
    Write-Verbose "Output is identical or close enough to fool the test cases"
    $testsArray += New-TestCase -Name "Output Match" -Output "Your output matched the test cases exactly or at least close enough to trick them.  Great work." -Visibility "visible" -status 'passed' -score 5.0

} else {
    Write-Verbose "Output does not match expected result."
    $testsArray += New-TestCase -Name "Output Mismatch" -Output @"
    Test output: 
    ``````
    $expectedresult
    ``````
    Your Output:
    ``````
    $testLaunch
    ``````
"@ -Visibility "visible" -status 'failed' -OutputFormat 'md'
}

return WriteAndSaveTest -results $results -testsArray $testsArray
