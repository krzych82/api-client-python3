import urllib.request
import urllib.parse
import collections
import base64
import hmac
import hashlib

class Client():
    def __init__(self, api_token, api_secret, api_host='https://api.tme.eu'):
        self.__api_token = api_token
        self.__api_secret = api_secret.encode()
        self.__api_host = api_host

    def __get_signature_base(self, url, params):
        params = collections.OrderedDict(sorted(params.items()))
        encoded_params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        signature_base = 'POST' + '&' + urllib.parse.quote(url, '') + '&' + urllib.parse.quote(encoded_params, '')
        return signature_base.encode()

    def __calculate_signature(self, url, params):
        hmac_value = hmac.new(self.__api_secret, self.__get_signature_base(url, params), hashlib.sha1).digest()
        return base64.encodebytes(hmac_value).rstrip()

    def request(self, endpoint, params, format='json'):
        url = self.__api_host + endpoint + '.' + format
        params['Token'] = self.__api_token
        params['ApiSignature'] = self.__calculate_signature(url, params)

        data = urllib.parse.urlencode(params).encode()
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }
        return urllib.request.Request(url, data, headers)