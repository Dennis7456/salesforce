import json
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType

loginInfo = json.load(open('login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

"""
Connect to SalesForce
"""

#sf = Salesforce(username=username, password=password, security_token=security_token, domain=domain)

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)

sf = Salesforce(instance_url=instance, session_id=session_id)
print(dir(sf))