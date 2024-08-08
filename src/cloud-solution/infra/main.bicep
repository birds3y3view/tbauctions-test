param accountName string
param blobName string
param sourceAccountName string
param sourceBlobName string
param location string
param adminLogin string
param serverName string
param sqlDBName string

module sourceData 'sourcedata.bicep' = {
  name: 'sourceDataMod'
  params: {
    sourceAccountName: sourceAccountName
    sourceBlobName: sourceBlobName
    location: location
  }
}

module storage 'storage.bicep' = {
  name: 'storageMod'
  params: {
    accountName: accountName
    blobName: blobName
    location: location
  }
}

module database 'database.bicep' = {
  name: 'databaseMod'
  params: {
    adminLogin: adminLogin
    adminLoginPass: 'password2123%$*@%'
    location: location
    serverName: serverName
    sqlDBName: sqlDBName
  }
}
