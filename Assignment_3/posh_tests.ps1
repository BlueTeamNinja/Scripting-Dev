# Out of 50
$score = 25.0
$minor = 5.0
$major = 10.0

$mistakes = @()

$filecount = 2

$submission_data = '/autograder/submission/*'
$files = get-childitem $submission_data

# Testing submissions

if($files.length -ne $filecount) {
    $score -= $major
    $mistakes = $mistakes + "Major: Incorrect number of files submitted."
}

$script = $files | Where-Object Extension -like ".ps1"
$data = $files | Where-object Extension -like ".csv"

    if($null -eq $script){
        $score = 0
        $mistakes = $mistakes + "Fail: No (or multiple) powershell script(s) detected.  There is nothing to grade."

        $autograder_results = New-Object -TypeName PSObject -Property @{
            score = $score
            output = "$($mistakes | %{$_ + "`n"})"
        }
        
        $autograder_results | ConvertTo-Json | Out-File '/autograder/results/results.json' -Force
        return 0
    }

    if($null -eq $data){
        $score = 0
        $mistakes = $mistakes + "Fail: No (or multiple) data file(s) detected.  There is nothing to grade."

        $autograder_results = New-Object -TypeName PSObject -Property @{
            score = $score
            output = "$($mistakes | %{$_ + "`n"})"
        }
        
        $autograder_results | ConvertTo-Json | Out-File '/autograder/results/results.json' -Force
        return 0
    }

    if($script.name -ne "assignment_3.ps1"){
        $score -= $major
        $mistakes = $mistakes + "Major: Powershell script detected, but invalid script name.  The grader is attempting to guess your submission."
    }

    if($data.name -ne 'organizations-1000.csv'){
        $score -= $major
        $mistakes = $mistakes + "Major: Data file detected but with an invalid name.  The grader is attempting to guess your submission."
    }
    
# Running some simple powershell commands. 
Copy-Item -Path $submission_data -Destination ./ -Recurse -Force

# Testing OUTPUT


# dot source the submission file
try{
$testcase = . $script[0].FullName "Computer*"
}catch{
    if($null -eq $script){
        $score = 0
        $mistakes = $mistakes + "Fail: Script did not execute without errors.  The MOST likely, but not the only possible cause: You referenced a file that does not exist on this system.  BIG HINT:  If you used an ``absolute`` file path in this assignment, your script will not execute in the autograder."

        $autograder_results = New-Object -TypeName PSObject -Property @{
            score = $score
            output = "$($mistakes | ForEach-Object{$_ + "`n"})"
        }
        
        $autograder_results | ConvertTo-Json | Out-File '/autograder/results/results.json' -Force
        return 0
    }
}

    if(-not($query -like 'Computer*')){
            $score = $score-$minor
            $mistakes = $mistakes + 'Minor: $query variable not used'
        }

    if($null -eq $output){
            $score = $score-$minor
            $mistakes = $mistakes + 'Minor: $output variable not used'

    }

    if($($testcase | Measure-Object).count -ne 32){
        $score = $score-$major
        $mistakes = $mistakes + "Major: Incorrect results, tested using `'Computer*' which should have 32 items"
    }


## Build autograder output
if($score -lt 0.0){ $score = 0.0}
$autograder_results = New-Object -TypeName PSObject -Property @{
    score = $score
    output = "$($mistakes | ForEach-Object {$_ + "`n"})"
}
Write-Output "Output from test"
$output

Write-Output "Query"
$query

Write-Output "Mistakes"
$mistakes

$autograder_results | ConvertTo-Json | Out-File '/autograder/results/results.json' -Force