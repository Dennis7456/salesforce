from importlib.metadata import metadata
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
 
"""
Salesforce ord info
"""
for element in dir(sf):
    if not element.startswith('_'):
        if isinstance(getattr(sf, element), str):
            print('Property Name: {0} Value: {1}'.format(element, getattr(sf, element)))

"""
Salesforce metadata
"""
metadata_org = sf.describe()
print(metadata_org['encoding'])
print(metadata_org['maxBatchSize'])
print(metadata_org['sobjects'])

df_sobjects = pd.DataFrame(metadata_org['sobjects'])
df_sobjects.to_csv('orgmetadata.csv', index=False)

#method 1
account = sf.account
account_metadata = account.describe()
df_account_metadata = pd.DataFrame(account_metadata.get('fields'))
df_account_metadata.to_csv('accountobjectmetadata.csv', index=False)

#method 2
project = SFType('Project__c', session_id, instance)
project_metadata = project.describe()
