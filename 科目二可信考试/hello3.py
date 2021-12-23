import json

a = ["阿松大","阿松士大夫"]

b = json.dumps(a,ensure_ascii=False)
print(b)

with open("test.txt",mode="r+",encoding="utf-8") as f:
    f.write(b)