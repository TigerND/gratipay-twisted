#
# -*- coding: utf-8 -*-
#

import pkg_resources
try:
    version=pkg_resources.get_distribution('txgratipay').version
except:
    version="0.0.0"


import api