import requests

class BearerAuth(requests.auth.AuthBase):

    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

#GET

api_url = "https://gorest.co.in/public/v2/users/3061"
response = requests.get(api_url)
print(response.json())
print(response.status_code)


#POST

# api_url = "https://gorest.co.in/public/v2/users"
# todo = {
#     "id": 3061,
#     "name": "Amelia X",
#     "email": "gggg@yahoo.com",
#     "gender": "female",
#     "status": "inactive"
#         }
# response = requests.post(api_url, json=todo, auth=BearerAuth('3211851a79084b29fb93a85047caf8873f37ea803a3df632be03fb54be5762a0'))
# print(response.json())
# print(response.status_code)

#PUT

# api_url = "https://gorest.co.in/public/v2/users/3061"
# todo = {
#     "id": 3061,
#     "name": "Amelia XY",
#     "email": "gggg@yahoo.com",
#     "gender": "female",
#     "status": "active"
#         }
# response = requests.put(api_url, json=todo, auth=BearerAuth('3211851a79084b29fb93a85047caf8873f37ea803a3df632be03fb54be5762a0'))
# print(response.json())
# print(response.status_code)

#PATCH

# api_url = "https://gorest.co.in/public/v2/users/3061"
# todo = {
#     "email": "gggg@outlook.com",
#     "status": "inactive"
#         }
# response = requests.patch(api_url, json=todo, auth=BearerAuth('3211851a79084b29fb93a85047caf8873f37ea803a3df632be03fb54be5762a0'))
# print(response.json())
# print(response.status_code)

#DELETE

# api_url = "https://gorest.co.in/public/v2/users/3061"
# response = requests.delete(api_url)
# print(response.json())
# print(response.status_code)