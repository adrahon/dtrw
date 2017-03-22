from .connection import Connection
from .accounts import Account

class DTR(object):
    """
    The Dtr class provides access to a DTR and its API
    """

    def __init__(self, dtr_host):
        self._connection = Connection(dtr_host)

    def self_signed(self):
        self._connection.self_signed()
            
    def credentials(self, username, password):
        self._connection.credentials(username, password)

    def users(self, accfilter='', start='', limit=100):
        if accfilter not in ['admins', 'non-admins']:
            accfilter='users'

        request = "accounts/"
        payload = {'filter': accfilter, 'start': start, 'limit': limit}
        r = self._connection.get(request, payload=payload, endpoint='enzi')
        users = []
        for u in r.json()['accounts']:
            users.append(Account.fromdic(u))
        return users

    def add_user(self, name, password, fullname='', admin=False):
        acc = Account(name, fullname=fullname, org=False, admin=admin)
        acc.add(self._connection, password)
        return self.load_user(name)

    def delete_user(self, name):
        Account(name).delete(self._connection)

    def load_user(self, name):
        return Account.load(self._connection, name)

