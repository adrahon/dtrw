import requests

class Connection(object):
    """
    A class to manage connection and requests to the DTR
    """

    def __init__(self, dtr_host, username="", password=""):
        self._dtr_host = dtr_host
        self._base_url= {
                'api':  "https://" + dtr_host + "/api/v0/",
                'enzi': "https://" + dtr_host + "/enzi/v0/"}
        self._username = username 
        self._password = password

    def self_signed(self):
        """
        DTR uses self-signed certificates, suppress warning
        """
        from requests.packages.urllib3.exceptions import SubjectAltNameWarning
        requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)

    def credentials(self, username, password):
        self._username = username
        self._password = password

    def get(self, request='', payload='', endpoint='api'):
        r = requests.get(self._base_url[endpoint] + request, params=payload,
                auth=(self._username, self._password))
        if r.ok:
            return r
        else:
            r.raise_for_status()

    def post(self, request='', payload='', endpoint='api'):
        r = requests.post(self._base_url[endpoint] + request, json=payload,
                auth=(self._username, self._password))
        if r.ok:
            return r
        else:
            r.raise_for_status()

    def delete(self, request='', payload='', endpoint='api'):
        r = requests.delete(self._base_url[endpoint] + request, params=payload,
                auth=(self._username, self._password))
        if r.ok:
            return r
        else:
            r.raise_for_status()

