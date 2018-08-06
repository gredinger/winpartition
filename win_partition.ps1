$params = Parse-Args $args

$drive_letter = Get-AnsibleParam -obj $params -name "drive_letter" -type "str" -default "C"

$result = @{
    changed = $false
}

$size = Get-PartitionSupportedSize -DriveLetter $drive_letter
$disk = Resize-Partition -DriveLetter $drive_letter -Size $size.SizeMax
if($?) {
    changed = $true
        Exit-Json -obj $result
    } else {
        if ($error[0].ToString() -like "*already the requested size*") {
            Exit-Json -obj $result
    }
}
