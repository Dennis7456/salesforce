import pandas as pd
from salesforce_bulk import SalesforceBulk
import json
import time
from salesforce_bulk.util import IteratorBytesIO

loginInfo = json.load(open('login.json'))

username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
# sandbox = loginInfo['sandbox']

bulk = SalesforceBulk(username=username, password=password, security_token=security_token)

job = bulk.create_query_job("Contact", contentType='JSON')
# batch = bulk.query(job, "select Id,LastName,Email from Contact")
batch = bulk.query(job, "select Email from Contact")
bulk.close_job(job)
while not bulk.is_batch_done(batch):
    time.sleep(10)

for result in bulk.get_all_results_for_query_batch(batch):
    result = json.load(IteratorBytesIO(result))
    for row in result:
        print(row) # dictionary rows

