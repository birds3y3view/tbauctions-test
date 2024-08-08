$context = New-AzStorageContext -StorageAccountName 'tbasourceaccount20240808' -Protocol Https

foreach ($file in Get-ChildItem "../data")
    {
        Set-AzStorageBlobContent `
        -File "../data/$file" `
        -Container "tbasource" `
        -Blob "$file" `
        -Context $context
    }