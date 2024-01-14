Describe 'A1E1 PowerShell Script Tests' {
    BeforeAll {
        # Path to the student's submission
        $scriptPath = 'A1E1.ps1'
        # Read the script and remove comments and blank lines
        $scriptLines = Get-Content $scriptPath | Where-Object { $_ -notmatch '^\s*#' -and $_.Trim() -ne '' }
    }

    It "Lists .pptx files in Documents" {
        $command = $scriptLines[0] 
        { Invoke-Expression $command } | Should -Not -Throw
        $result = Invoke-Expression $command
        $result.Name | Should -Contain '*.pptx'
    }

    It 'Lists files in the current directory' {
        $command = $scriptLines[1]
        { Invoke-Expression $command } | Should -Not -Throw
        $result = Invoke-Expression $command
        $result.Count | Should -BeGreaterThan 0
    }

    It 'Creates a new directory PSTemp' {
        $command = $scriptLines[2]
        { Invoke-Expression $command } | Should -Not -Throw
        Test-Path './PSTemp' | Should -Be $true
    }

    It 'Creates multiple directories in root' {
        $command = $scriptLines[3]
        { Invoke-Expression $command } | Should -Not -Throw
        Test-Path '/ExampleDirOne' | Should -Be $true
        Test-Path '/ExampleDirTwo' | Should -Be $true
    }

    It 'Creates a new file MonsterBash.txt in PSTemp' {
        $command = $scriptLines[4]
        { Invoke-Expression $command } | Should -Not -Throw
        Test-Path './PSTemp/MonsterBash.txt' | Should -Be $true
    }

    It 'Creates a file with spaces in its name in PSTemp' {
        $command = $scriptLines[5]
        { Invoke-Expression $command } | Should -Not -Throw
        Test-Path './PSTemp/Monster Bash.txt' | Should -Be $true
    }

    It 'Gets help for Get-Location' {
        $command = $scriptLines[6]
        { Invoke-Expression $command } | Should -Not -Throw
    }

    It 'Gets online help for Stop-Process' {
        $nobrowser = "Starting a browser to display online Help failed. No program or browser is associated to open the URI https://go.microsoft.com/fwlink/?LinkID=2097058."
        $command = $scriptLines[7]
        { Invoke-Expression $command } | Should -Throw $nobrowser
    }

    It 'Stops processes starting with note' {
        $command = $scriptLines[8]
        { Invoke-Expression $command } | Should -Not -Throw
    }

    It 'Writes PowerShell version' {
        $command = $scriptLines[9]
        { Invoke-Expression $command } | Should -Not -Throw
        $result = Invoke-Expression $command
        $result | Should -Not -BeNullOrEmpty
    }

    It 'Writes the favorite keyboard key' {
        $command = $scriptLines[10]
        { Invoke-Expression $command } | Should -Not -Throw
        $result = Invoke-Expression $command
        $result | Should -Be '[TAB]'
    }
}
