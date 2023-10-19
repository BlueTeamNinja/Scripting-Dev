$search_directory = $args[0]
$files_to_search = Join-Path $search_directory "*.csv"
$email_rows = Select-String -path $files_to_search -Pattern '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
$email_count = ($email_rows | Measure-Object).count
Write-Output "Searching all .txt files in $search_directory for email addresses..."
Write-Output "$email_rows"
Write-Output "$email_count emails were found."