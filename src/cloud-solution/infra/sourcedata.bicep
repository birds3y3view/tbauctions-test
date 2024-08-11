param sourceAccountName string
param sourceBlobName string
param location string

resource sourceStorageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: sourceAccountName
  location: location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
}

resource sourceBlobService 'Microsoft.Storage/storageAccounts/blobServices@2023-05-01' = {
  parent: sourceStorageAccount
  name: 'default'
}

resource sourceBlobContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  parent: sourceBlobService
  name: sourceBlobName
}
