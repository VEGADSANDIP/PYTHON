import json

# file=open('64KB.json','r')
# x = file.read()
# data = json.loads(x)

# for i in data:
#     print(i["name"])

# file = open('sample-json-file.json','r');
# data = file.read()
# x = json.loads(data);
# for i in x:
    # print(i,x[i])
    # print(i["name"])


# data = open('Sample-JSON-file-with-multiple-records-download.json','r')
# asd = data.read()
# v = json.loads(asd)

# for i in v:
#     print(v[i])



var = open('sample-json-files-sample1.json','r')
x =var.read()
a = json.loads(x)
print(a["size"])