This repository is maintained for the **deprecated version of the TME API only** and is no longer updated with the latest API documentation.

For the current API version (v2), please refer to the official documentation available:
- via the [**Developer Portal**][developers-website]
- directly at [documentation page][documentation-website]

To ensure you are using the latest endpoints, authentication flow, and integration guidelines, always refer to the official TME API v2 documentation.

## Examples

Simple request:

```
import tmeapi
import urllib.error
import urllib.request

token = '<YOUR_TOKEN>'
secret = '<YOUR_SECRET>'

client = tmeapi.Client(token, secret)
parameters = {
    'SymbolList[0]': 'AX-176',
    'SymbolList[1]': '1N4007-DIO',
    'Country': 'GB',
    'Language': 'EN',
}

try:
    response = urllib.request.urlopen(client.request('/Products/GetProducts', parameters))
    print(response.read())
except urllib.error.URLError as e:
    print(e.reason)
```

See TME API [documentation][documentation-website] for more details.

[developers-website]: https://developers.tme.eu
[documentation-website]: https://api-doc.tme.eu/v2