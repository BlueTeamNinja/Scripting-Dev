# Initialize variables
$submission_data = '/autograder/submission/*'
$files = Get-ChildItem $submission_data
$expectedScriptName = "A0E1.ps1"
$tests = @()

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

# Check if the correct file is submitted
$script = $files | Where-Object Name -eq $expectedScriptName
$scriptContent = Get-Content $script

if ($null -eq $script) {
    Add-TestResult "File Name Check" 0 10 "failed" "Failed: Script '$expectedScriptName' not found. Ensure the file name is correct and case-sensitive."
} else {
    Add-TestResult "File Name Check" 10 10 "passed" "Your script has the correct filename"
    # Additional checks can be performed here
}


# Check for the name change
if($scriptContent -match '\$name\s*=\s*"Abe"'){
    Add-TestResult "Checking Name Change" 0 10 "failed" "Major Fault: You need to change the name from 'Abe' to something else in your script."
} elseif($scriptContent -match '\$name\s*=\s*"\[Your Name\]"'){
    Add-TestResult "Checking Name Change" 0 10 "failed" "Silly: You've been extremely literal by using '[Your Name]'. Creative, but remember to use a different name."
} else {
    Add-TestResult "Checking Name Change" 10 10 "passed" "You correctly changed it to your own name!"

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
