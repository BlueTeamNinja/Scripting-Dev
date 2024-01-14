# Scripting Fundamentals

Running in docker

`$A` = Assignment Number  
`$P` = Assignment Path
`$I` = Docker image (Lazily just loads first)

Run first:
```
$A='0';
$P="$($PWD.path)/Assignment_$A/";
docker run -it -v "$P/samples:/autograder/submission" -v "$P/results:/autograder/results" -v "$P/build/:/autograder/source" gradescope/autograder-base:latest /autograder/source/setup.sh
```

```
$A='0';
$P="$($PWD.path)/Assignment_$A/";
$i = docker images --format="{{.ID}}" | Select-Object -First 1;
docker run -it -v "$P/samples:/autograder/submission" -v "$P/results:/autograder/results" -v "$P/build/:/autograder/source" $i /autograder/run_autograder
Write-Output "$P/results/results.json" | ConvertFrom-Json
```
