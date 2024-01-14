# Define the answer key
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

$answerKey = @(
    "Get-ChildItem -Path 'Documents' -Filter *.pptx", # Example Command
    "Get-ChildItem",                                # Command 1
    "New-Item -Path 'PSTemp' -ItemType Directory",  # Command 2
    "New-Item -Path '/ExampleDirOne', '/ExampleDirTwo' -ItemType Directory", # Command 3
    "New-Item -Path './PSTemp/' -Name 'MonsterBash.txt' -ItemType File",     # Command 4
    "New-Item -Path './PSTemp/' -Name 'Monster Bash.txt' -ItemType File",    # Command 5
    "Get-Help Get-Location",                       # Command 6
    "Get-Help Stop-Process -Online",               # Command 7
    "Stop-Service -Name 'note*'",                  # Command 8
    "Write-Output `$PSVersionTable.PSVersion",      # Command 9
    "Write-Output '[TAB]'"                         # Command 10
)

# Define the initial test results structure
$results = @{
    output             = "Thank you for your submission."
    output_format      = "simple_format"
    test_output_format = "md"
    test_name_format   = "simple_format"
    visibility         = "visible"
    stdout_visibility  = "visible"
    extra_data         = @{}
}

# Initialize an array to store test cases
$testsArray = @()

# Read the student's submission and filter out blank lines and comments
$submissionContent = Get-Content -Path "/autograder/submission/A1E1.ps1" | 
                     Where-Object { $_ -and $_.Trim() -notmatch '^\s*#' }

# Process the submission and create test cases
for ($i = 0; $i -lt $answerKey.Count; $i++) {
    $expected = $answerKey[$i]
    $studentResponse = $submissionContent[$i]

    $status = if ($studentResponse -and ($studentResponse -replace '\s+', ' ').Trim().ToLower() -eq $expected.ToLower()) { "passed" } else { "failed" }
    $output = if ($status -eq "failed") { "Expected:`n$expected`nReceived:`n$studentResponse" } else { "You matched exactly, great job!" }
    $score = if ($status -eq "passed") { 5.0 } else { 0.0 }

    Write-Output "Expected $expected`nAnswer: $answerKey[$i]"
    $testsArray += New-TestCase -Name ("Command " + ($i + 1)) -Output $output -Score $score -MaxScore 10 -Status $status
}

# Save the test results to a JSON file
WriteAndSaveTest -results $results -testsArray $testsArray
