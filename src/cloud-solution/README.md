### Infrastructure requirements
1. A source location for the data files
2. A storage location to land the data files and export processed files
3. A Database in which to perform data processing activities
4. A reporting layer for displaying 2 distributions

### Functionality Requirements
1. Copy source data to a 'raw' 'folder' converting to parquet
2. Clean the source data and output as files to a 'clean' 'folder'
3. Convert the cleaned data to a star schema structure and output to a 'reporting' 'folder'

### Deployment Guide
To deploy the stack run the following code from the infra directory:
```
.\deployment.ps1
```

### Cleaning up
When you are finished, you can completely remove the stack with the following command:
```
.\clean.ps1
```

### Extra info
If you want to access the database using a tool such as DBeaver, you need to Whitelist your IP on the SQL Server

If you want to access and upload data to the blob, you must add the appropriate IAM roles to your account