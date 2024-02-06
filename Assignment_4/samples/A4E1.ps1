# Get the directory path from the command line parameters
$search_dire = $args[0]

# Print a sentence that tells the user what the script is doing
Write-Output "Searching all .txt files in $search_dire for email addresses..."

# Combine the directory path and the wildcard filter to search only in .txt files
$files_to_search = Join-Path $search_dire "*.csv"

# Search all .txt files in the specified directory for valid email addresses
$email_rows = Select-String -Path $files_to_search -Pattern "[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
$email_count = ($email_rows | Measure-Object).count
Write-Output $email_rows
Write-Output "$email_count emails were probably found." 
