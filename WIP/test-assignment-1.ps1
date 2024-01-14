Import-Module Pester
$configuration = [PesterConfiguration]@{
    Run = @{
        Path = "./tests/*.ps1"
        PassThru = $true
    }
    Output = @{
        Verbosity = 'Detailed'
    }
    Should = @{
        ErrorAction = 'Continue'
    }
    CodeCoverage = @{
        Enable = $true
        OutputPath = "./test.json"
    }
}

# Run the tests and transform output to the required format
$results = Invoke-Pester -Configuration $configuration
$customResults = $results.Tests | ForEach-Object {
    @{
        Name = $_.Name
        Testing = $_.ScriptBlock.ToString()
        Status = if ($_.Passed) { "passed" } else { "failed" }
        Output = if (-not $_.Passed) { $_.ErrorRecord }
    }
}

# Convert to JSON and write to file
$customResults | ConvertTo-Json | Out-File "results.json"
