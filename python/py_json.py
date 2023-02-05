# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample json 
userJSON_NM ='{"first_name": "lana" ,"last_name":"mohammed","age": 16 }'

#parse to dic 
user_NM = json.loads(userJSON_NM)
#print(user_NM['first_name'])
#print(user_NM)

car_NM = {'make': 'ford','model':'mustange','year': 1980 } 
carJSON_NM = json.dumps(car_NM)
print(carJSON_NM)
