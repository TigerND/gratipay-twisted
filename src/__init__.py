#
# -*- coding: utf-8 -*-
#

import pkg_resources
try:
    version=pkg_resources.get_distribution('txgittip').version
except:
    version="0.0.0"


import api