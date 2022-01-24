import requests
import json

response = requests.get(
    "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1FF36BFA-6E91-47B0-B2DB-33918E626906&format=JSON")
a = response.json()
# print(a["records"]["location"][0]["locationName"])
for i in a["records"]["location"]:
    print(i["locationName"])

