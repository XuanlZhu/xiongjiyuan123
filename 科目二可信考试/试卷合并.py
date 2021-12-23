import json

with open("shi.txt",mode="r",encoding="utf-8") as f:
    s = f.read()

a = json.loads(s)
print(a)
with open("test.txt",mode="r",encoding="utf-8") as f:
    s = f.read()

a2 = json.loads(s)
print(a2)

for i in a2:
    if i not in a:
        a.append(i)


with open("tem.json", mode="r+", encoding="utf-8") as f:
    f.write(json.dumps(a,ensure_ascii=False))


