import requests
import  json
status ='available'

# res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

if 'application/json' in res.headers['Content-Type']:
    res.json()
else:
    res.text
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
url =
headers = {'accept': 'application/json'}
res = requests.post(url, headers=headers, data=data)

