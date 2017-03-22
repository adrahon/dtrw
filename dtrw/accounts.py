import json

class Account(object):

    def __init__(self, name, a_id='', fullname='', org=False, admin=False,
            active=True):
        self.name = name
        self.id = a_id
        self.fullname = fullname
        self.org = org
        self.admin = admin
        self.active = active

    @classmethod
    def fromdic(cls, dic):
        if dic['isOrg']:
            return cls(dic['name'], dic['id'], dic['fullName'], True)
        else:
            return cls(dic['name'], dic['id'], dic['fullName'], False,
                        dic['isAdmin'], dic['isActive'])

    @classmethod
    def load(cls, connection, name):
        request = "accounts/{name}"
        r = connection.get(request.format(name=name), endpoint='enzi')
        return cls.fromdic(r.json())

    def add(self, connection, password=''):
        request = "accounts"
        payload = {'name': self.name, 'fullName': self.fullname, 'isOrg':
                self.org, 'isAdmin': self.admin, 'isActive': self.active,
                'password': password}
        return connection.post(request, payload=payload, endpoint='enzi')

    def delete(self, connection):
        request = "accounts/{name}".format(name=self.name)
        r = connection.delete(request, endpoint='enzi')
        if r.ok:
            self.id = ''
        else:
            r.raise_for_status()
