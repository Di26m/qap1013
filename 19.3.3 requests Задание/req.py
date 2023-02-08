import requests
import json
status ='available'

# res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})


print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

qqq=res.json()
print(qqq[0]['id'])

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_post = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data=json.dumps(info, ensure_ascii=False))

print(res_post.status_code)
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))


petId = info.get('id')
res_del = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId}")

print(res_del.status_code)
print(res_del.text)
print(res_del.json())
print(type(res_del.json()))

new_info = {
  "id": 444,
  "category": {
    "id": 0,
    "name": "snake"
  },
  "name": "Umbertinio",
  "photoUrls": [
    "no foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
petId = qqq[0]['id']
# res_put = requests.put(f"https://petstore.swagger.io/v2/pet/{petId}",
#     headers={'accept': 'application/json', 'Content-Type': 'application/json'},
#     data=json.dumps(new_info, ensure_ascii=False))

res_put = requests.put(f"https://petstore.swagger.io/v2/pet/{petId}",
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    data=json.dumps(new_info, ensure_ascii=False))

print(res_put.status_code)
print(res_put.text)
print(res_put.json())
print(type(res_put.json()))