import json


dict = {
    "name":"sandip",
    "age":24
}
print(f"{type(dict)}\n{(dict)}")

a = json.dumps(dict)
print(f"{type(a)}\n{(a)}")