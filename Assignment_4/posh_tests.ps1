# PowerShell function to generate the 'tests' portion
function New-TestCase {
    param (
        [Parameter(Mandatory=$true)][string]$Name,
        [Parameter(Mandatory=$true)][string]$Output,
        [Parameter(Mandatory=$true)][double]$Score,
        [double]$MaxScore,
        [string]$Visibility,
        [string]$Status,
        [string]$Number,
        [string[]]$Tags,
        [hashtable]$ExtraData
    )

    # Create a test case object
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

    # Return the test case object
    return $testCase
}

$testsArray = @()

## ** Test 1 - Proper Filename ** 
$submissionFolder = '/autograder/submission/*'
$submission = get-childitem $submissionFolder

if($submission.length -gt 1){
    $testsArray += New-TestCase -Name "Count submissions" -Output "Too many files submitted" -Score -5.0 -Status 'failed'
}

if($submission[0].Name -like "assignment_4.ps1"){
    $testsArray += New-TestCase -Name "Correct Filename" -Output "Your submission contains the correct filename" -Status 'passed'
}

try{
    $testLaunch = . $submission[0].FullName '/autograder/submission/'
    $testLaunch_notrail = . $submission[0].FullName '/autograder/submission'

        if($testLaunch -ne $testLaunch_notrail){
            $testsArray += New-TestCase -Name "Trailing slash test" -Output "Your submission produces different results with or without a trailing slash." -Score -5.0 -Status 'failed'

        }

    }catch{
        $testsArray += New-TestCase -Name "**FAIL** - Script Execution" -Output "Your submission did not successfully execute.  This means it cannot be graded and results in a grade of 0." -Score -50.0 -Status 'failed'

    }

$test2 = New-TestCase -Name "Test2" -Output "Another output" -Visibility "visible" -Score 2.0

# Combine the tests into an array

# Create the main JSON structure
$results = @{
    #score              = 44.0
    #execution_time     = 136
    output             = "Thank you for your submission."
    output_format      = "simple_format"
    test_output_format = "simple_format"
    test_name_format   = "simple_format"
    visibility         = "visible"
    stdout_visibility  = "visible"
    extra_data         = @{}
    tests              = $testsArray
}

# Convert the results to JSON format
$jsonData = $results | ConvertTo-Json -Depth 4

# Save the JSON data to results.json
#$jsonData | Out-File -Path "results.json" -Encoding utf8
$jsonData