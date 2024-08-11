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
landrawdata.main()
dbloadraw.main()

# Clean Data Steps
cleanauctions.main()
cleanbids.main()
cleanbuyers.main()
dbloadclean.main()

# Reporting Data Steps
convertschema.main()
exportreporting.main()

# Visualisation Data Steps
buildreports.main()