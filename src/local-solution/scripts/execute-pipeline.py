import sys

sys.dont_write_bytecode = True

import dataloading.landrawdata as landrawdata
import dataloading.dbloadraw as dbloadraw

import datacleaning.cleanauctions as cleanauctions
import datacleaning.cleanbids as cleanbids
import datacleaning.cleanbuyers as cleanbuyers
import datacleaning.dbloadclean as dbloadclean

import datareporting.convertschema as convertschema
import datareporting.exportreporting as exportreporting

import datareporting.buildreports as buildreports

# Land Raw Data Steps
print("\n##### PIPELINE STARTING #####\n")

print("##### LANDING PHASE #####")
print("Importing Data to RAW Directory")
landrawdata.main()
print("Import Successful")
print("Loading Raw data into DB")
dbloadraw.main()
print("Load Successful")
print("##### LANDING COMPLETE #####\n")

# Clean Data Steps
print("##### CLEANING PHASE #####")
print("Cleaning Auctions")
cleanauctions.main()
print("Cleaning Bids")
cleanbids.main()
print("Cleaning Buyers")
cleanbuyers.main()
print("Loading Clean data into DB")
dbloadclean.main()
print("Load Successful")
print("##### CLEANING COMPLETE #####\n")

# Reporting Data Steps
print("##### REPORTING PHASE #####")
print("Converting data to star schema")
convertschema.main()
print("Exporting reporting tables to REPORTING Directory")
exportreporting.main()
print("##### REPORTING COMPLETE #####\n")

# Visualisation Data Steps
print("##### VISUALIZATION PHASE #####")
print("Building & exporting visuals")
buildreports.main()
print("##### VISUALIZATION COMPLETE #####\n")

print("##### PIPELINE COMPLETE#####\n")