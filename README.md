## TxGittip
Library for accessing [Gittip](https://www.gittip.com/) APIs

## Simple example
```py
import txgittip

@inlineCallbacks
def getUserInfo(username='Gittip')
    requests = [txgittip.api.public(username), txgittip.api.stats(username)]
    results = yield gatherResuts(requests)
    returnValue(results)
```

## Examples
For more examples please see [DTX Gittip Example](https://github.com/TigerND/dtx-examples/tree/master/gittip)

## License
LGPL v3
