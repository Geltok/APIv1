import requests
import json

status = 'available'
res = requests.get(f"https://petstore.swagger.io/#/pet/findPetsByStatus?status={status}",
                   headers={'accept': 'application/json'})
print(res.json)
print(res.text)

res_post = requests.post(f"https://petstore.swagger.io/#/pet",
                         headers={"accept": "application/json", "Content-Type": "application/json"})
print(res_post.json)
print(res_post.text)

res_put = requests.put(f"https://petstore.swagger.io/#/pet/updatePet",
                       headers={"accept": "application/json", "Content-Type": "application/json"})
print(res_put.json)
print(res_put.text)

res_delete = requests.delete(f"https://petstore.swagger.io/#/pet/deletePet",
                             headers={"accept": "application/json", "Content-Type": "application/json"})
print(res_delete.json)
print(res_delete.text)
