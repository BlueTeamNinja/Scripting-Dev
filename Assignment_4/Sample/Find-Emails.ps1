# Get the directory path from the command line parameters
$dir_path = $args[0]

# Print a sentence that tells the user what the script is doing
Write-Output "Searching all .txt files in $dir_path for email addresses..."

# Combine the directory path and the wildcard filter to search only in .txt files
$files_to_search = Join-Path $dir_path "*.csv"

# Search all .txt files in the specified directory for valid email addresses
Select-String -Path $files_to_search -Pattern "[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"