#!/usr/bin/env python3
import dtrw
import requests
import os

dtr = dtrw.DTR(dtr_host = os.environ['DTRHOST'])
dtr.credentials(username=os.environ['DTRUSER'],
        password=os.environ['DTRPASS'])
dtr.self_signed()

for user in dtr.users():
    if user.active:
        active = "Active"
    else:
        active = " ---- "
    print(user.id + ":  " + user.name + "   " + user.fullname + "   " + active)

newuser = dtr.add_user('johndoe', 's3cr3tp@ssw0rd', fullname='John Doe')
print("\n" + newuser.id + ":  " + newuser.name + "   " + newuser.fullname)

dtr.delete_user(newuser.name)

try:
    john = dtr.load_user('johndoe')
except requests.exceptions.RequestException as err:
    print(err)
