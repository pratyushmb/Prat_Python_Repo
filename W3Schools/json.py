import json

# some JSON value
x = '{"name":"roy", "age":30, "city":"kolkata"}'

y = json.loads(x)

print(y)
print(y["age"])

# convert from python to json

import json

x = {"name": "proy", "age": 30, "city": "kolkata"}

y = json.dumps(x)
print(y)
