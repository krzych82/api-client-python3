## Examples

Simple request:

```
import tmeapi
import urllib.error

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

See TME API [documentation][developers-tme] for more details.

[developers-tme]: https://developers.tme.eu/en/