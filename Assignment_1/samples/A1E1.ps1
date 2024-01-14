# Name: Example Student
# Student ID: 12345678
# Section: 1

### Example Question
Get-ChildItem -Path 'Documents' -Filter *.pptx

### Command 1
Get-ChildItem

### Command 2
New-Item -Path 'PSTemp' -ItemType Directory

### Command 3
New-Item -Path '/ExampleDirOne', '/ExampleDirTwo' -ItemType Directory

### Command 4
New-Item -Path './PSTemp/' -Name 'MonsterBash.txt' -ItemType File

### Command 5
New-Item -Path './PSTemp/' -Name 'Monster Bash.txt' -ItemType File

### Command 6
Get-Help Get-Location

### Command 7
Get-Help Stop-Process -Online

### Command 8
Stop-Service -Name 'note*'

### Command 9
Write-Output $PSVersionTable.PSVersion

### Command 10
Write-Output '[SPACE]'
