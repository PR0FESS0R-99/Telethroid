#  Telethroid - Telegram BoT Library for Python
#  Copyright (C) 2023-present Pr0fess0r-99 <https://github.com/Pr0fess0r-99>

__version__ = "0.0.11"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2023-present Pr0fess0r-99 <https://github.com/Pr0fess0r-99>"

import Telethroid.filters
import Telethroid.types
import Telethroid.errors

from Telethroid.client import TelethroidClient

def started_telethroid():
  print(
    "Telethroid Successfully Installed" + "\n"
    f"Version : {__version__}"
  )
