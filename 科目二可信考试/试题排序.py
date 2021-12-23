import json

with open("tem.json", mode="r", encoding="utf-8") as f:
    s = f.read()

a = json.loads(s)
b = []
c = []
for i in a:
    if "单选题" in i:
        b.append(i)
    elif "多选题" in i:
        c.append(i)


print(b+c)


with open("tem.json", mode="w", encoding="utf-8") as f:
    f.write(json.dumps(b+c,ensure_ascii=False))