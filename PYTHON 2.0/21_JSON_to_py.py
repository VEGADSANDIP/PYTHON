import json


j = '{"name":"sandip","age":24,"surname":"vegad"}'
print(f"{type(j)} {(j)}")


x = json.loads(j)
print(x,type(x))
