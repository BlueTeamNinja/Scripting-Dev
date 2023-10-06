## Execute using NumberOfFiles and NumberOfLines as parameters or you'll get a single entry

param (
    [int]$NumberOfFiles = 1,
    [int]$NumberOfLines = 1

)

function Get-RandomNames($count) {
    ##  Sorry for whitewashing the text but it was easier than replacing invalid characters in emails. 
    $uri = "https://randomuser.me/api/?inc=name,login&results=$count&nat=au,ca,nz,us"
    $response = Invoke-RestMethod -Uri $uri

    return $response.results | ForEach-Object {
        @{
            First = $_.name.first
            Last  = $_.name.last
            Username = $_.login.username
        }
    }
}

function Get-RandomSport {
    $sports = @("Basketball", "Football", "Baseball", "Tennis", "Golf", "Soccer", "Swimming", "Volleyball", "Rugby", "Hockey")
    return $sports | Get-Random
}

function Get-RealisticEmail {
    param (
        [string]$FirstName,
        [string]$LastName, 
        [string]$UserName
    )

    # Define potential email formats
    $emailFormats = @(
        '{0}{1}',
        '{0}.{1}',
        '{0}_{1}',
        '{0}{1:0}',
        '{0}.{1:0}',
        '{1}{0}',
        '{1}.{0}',
        '{1}_{0}',
        '{1}{0:0}',
        '{1}.{0:0}'
    )

    # Define potential domain names (both business-like and known free services)
    $domains = @(
        "example.com",
        "business.net",
        "company.org",
        "webpage.biz",
        "enterprise.info",
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "webtech.com", 
        "digitalfront.net", 
        "cloudpulse.org", 
        "datavirtue.biz", 
        "cyberneticweb.net", 
        "infotechline.com", 
        "netnexus.org", 
        "globaldataflow.net", 
        "codebyte.org", 
        "cybercentral.com", 
        "binarycore.net", 
        "virtualstacks.org", 
        "netwave.biz", 
        "futurebits.net", 
        "techgrid.com", 
        "webwarden.org", 
        "datarealm.biz", 
        "techtonic.net", 
        "digitaldynamo.com", 
        "netcrafters.org", 
        "codehaven.net", 
        "globalgrid.biz", 
        "quantumcode.net", 
        "siliconpulse.org", 
        "datadome.biz", 
        "netnode.org", 
        "cyberclime.net", 
        "infospherix.com", 
        "netnavigators.org", 
        "siliconshore.biz", 
        "techstreamline.com", 
        "cybercanvas.net", 
        "datadeck.org", 
        "webweaver.biz", 
        "codexcore.net", 
        "digitaldrift.org", 
        "netnavigator.com", 
        "virtualverse.net", 
        "techterrane.org", 
        "binaryblend.biz "
    )

    # 70% chance to use name-based format, 30% chance to use random username
    if ((Get-Random -Minimum 1 -Maximum 10) -le 7) {
        $emailFormat = $emailFormats | Get-Random
        $emailUser = $emailFormat -f $FirstName.ToLower(), $LastName.ToLower()
    } else {
        $emailUser = $UserName
    }

    $emailDomain = $domains | Get-Random
    return "$emailUser@$emailDomain"
    }

function Get-RandomContact {
    $methods = @("call", "text", "email")
    $selectedMethod = $methods | Get-Random

    switch ($selectedMethod) {
        "call" { 
            $phoneNumber = "({0:d3}) {1:d3}-{2:d4}" -f (Get-Random -Minimum 100 -Maximum 999), (Get-Random -Minimum 100 -Maximum 999), (Get-Random -Minimum 1000 -Maximum 9999)
            return @{ Method = $selectedMethod; Detail = $phoneNumber }
        }
        "text" {
            $phoneNumber = "({0:d3}) {1:d3}-{2:d4}" -f (Get-Random -Minimum 100 -Maximum 999), (Get-Random -Minimum 100 -Maximum 999), (Get-Random -Minimum 1000 -Maximum 9999)
            return @{ Method = $selectedMethod; Detail = $phoneNumber }
        }
        "email" {
            return @{ Method = $selectedMethod}
        }
    }
}

for ($i = 1; $i -le $NumberOfFiles; $i++) {
    $outputFile = "output_$i.csv"
    $csvData = @()

    $names = Get-RandomNames $NumberOfLines

    foreach ($name in $names) {
        $sport = Get-RandomSport
        $contact = Get-RandomContact

        if($contact.Method -eq "email"){
            $contact.Detail = Get-RealisticEmail -FirstName $name.First -LastName $name.Last -username $name.Username
        }
        $csvData += [PSCustomObject]@{
            'first name'    = $name.First
            'last name'     = $name.Last
            'sport'         = $sport
            'contact method'= $contact.Method
            'details'       = $contact.Detail
        }
    }

    $csvData | Export-Csv -Path $outputFile -NoTypeInformation
    Write-Output "Created $outputFile"
}
