import sys

sys.dont_write_bytecode = True

import cleanauctions
import cleanbids
import cleanbuyers

cleanauctions.main()
cleanbids.main()
cleanbuyers.main()
