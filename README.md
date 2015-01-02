## txgratipay
Library for accessing [Gratipay](https://www.gratipay.com/) APIs for the [Twisted](https://twistedmatrix.com/trac/) networking engine (written in Python)

## Simple example
```py
import txgratipay

@inlineCallbacks
def getUserInfo(username='gratipay')
    requests = [
        txgratipay.api.public(username), 
        txgratipay.api.stats(username),
    ]
    results = yield gatherResuts(requests)
    returnValue(results)
```

## Examples
For more examples please see [DTX Gratipay Example](https://github.com/TigerND/dtx-examples/tree/master/gratipay)

## License
LGPL v3
