Get-ChildItem -Recurse -Filter order.py | ForEach-Object {
    "===== $($_.FullName) =====" | Out-File output.txt -Append
    Get-Content $_.FullName | Out-File output.txt -Append
    "" | Out-File output.txt -Append
}