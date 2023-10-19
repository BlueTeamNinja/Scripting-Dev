$results = import-csv .\organizations-1000.csv
$query = $args[0]
$output = $results | Where-Object Industry -like $query
$output