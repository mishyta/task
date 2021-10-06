import requests
import json


response = requests.get("https://randomuser.me/api/") # A free, open-source API for generating random user data.

print(response.status_code) 

# Status codes:
# 200 OK 	
# 201 Created 	
# 400 Bad Request 	
# 401 Unauthorized 	
# 404 Not Found 	
# 405 Method Not Allowed 	
# 500 Internal Server Error 	




user = json.dumps(response.json(), indent=4)
print(user)



