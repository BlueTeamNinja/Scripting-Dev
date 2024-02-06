# Initialize variables
$score = 25.0
$minor = 5.0
$major = 10.0
$tests = @()
$submission_data = '/autograder/submission/*'
$files = Get-ChildItem $submission_data
$expectedScriptName = "A3E1.ps1"
$expectedDataName = 'organizations-1000.csv'

# Function to add a test result
function Add-TestResult {
    param ($name, $score, $max_score, $status, $output)
    $GLOBAL:tests += @{
        name = $name
        score = $score
        max_score = $max_score
        status = $status
        output = $output
    }
}

# Check if the correct number of files is submitted
if($files.Count -ne 2) {
    Add-TestResult "File Count Check" 0 $major "failed" "Major: Incorrect number of files submitted."
}

$script = $files | Where-Object Extension -like ".ps1"
$data = $files | Where-Object Extension -like ".csv"

# Check for Powershell script and data file
if($null -eq $script){
    Add-TestResult "Powershell Script Check" 0 $major "failed" "Fail: No (or multiple) powershell script(s) detected. There is nothing to grade."
} elseif($script.Name -ne $expectedScriptName) {
    Add-TestResult "Script Name Check" 0 $major "failed" "Major: Powershell script detected, but invalid script name. The grader is attempting to guess your submission."
} else {
    Add-TestResult "Script Name Check" $major $major "passed" "Script name is valid."
}

if($null -eq $data){
    Add-TestResult "Data File Check" 0 $major "failed" "Fail: No (or multiple) data file(s) detected. There is nothing to grade."
} elseif($data.Name -ne $expectedDataName) {
    Add-TestResult "Data File Name Check" 0 $major "failed" "Major: Data file detected but with an invalid name. The grader is attempting to guess your submission."
} else {
    Add-TestResult "Data File Name Check" $major $major "passed" "Data file name is valid."
}

# Copy the files to this directory to dot source properly
Set-Location /autograder/submission
# Dot source the submission file and execute tests
try {
    $testcase = . $script[0].FullName "Computer*"
    if(-not($query -like 'Computer*')){
        Add-TestResult "Query Variable Usage" 0 $minor "failed" 'Minor: $query variable not used'
    } else {
        Add-TestResult "Query Variable Usage" $minor $minor "passed" 'The $query variable is used correctly.'
    }

    if($null -eq $output){
        Add-TestResult "Output Variable Usage" 0 $minor "failed" 'Minor: $output variable not used'
    } else {
        Add-TestResult "Output Variable Usage" $minor $minor "passed" 'The $output variable is used correctly.'
    }

    if(($testcase | Measure-Object).Count -ne 32){
        Add-TestResult "Test Case Execution" 0 $major "failed" "Major: Incorrect results, tested using 'Computer*' which should have 32 items"
    } else {
        Add-TestResult "Test Case Execution" $major $major "passed" "Correct results for test case using 'Computer*'."
    }
} catch {
    Add-TestResult "Script Execution" 0 $major "failed" "Fail: Script did not execute without errors. The MOST likely, but not the only possible cause: You referenced a file that does not exist on this system. BIG HINT: If you used an ``absolute`` file path in this assignment, your script will not execute in the autograder.`n$ERROR"
}

# Function to write the results to a JSON file
function Write-JsonResult {
    param ([array]$tests)

    # Calculate total score
    $totalScore = ($tests | Measure-Object -Property score -Sum).Sum

    # Create the results object
    $autograder_results = @{
        tests = $tests
        visibility = "visible"
        score = $totalScore
    }

    # Convert to JSON and write to file
    $autograder_results | ConvertTo-Json -Depth 5 | Out-File '/autograder/results/results.json' -Force
}

# Write results
Write-JsonResult -tests $tests
