if ($null -eq (Get-AzResourceGroup -Name tba-assignment)) {
	New-AzResourceGroup -Name tba-assignment `
	 	-Location westeurope `
}
New-AzResourceGroupDeployment -Name deploy `
	-ResourceGroupName 'tba-assignment' `
	-TemplateFile .\main.bicep `
	-TemplateParameterFile .\parameters.json `
	-Verbose	