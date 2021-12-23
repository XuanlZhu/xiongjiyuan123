# body = [{"id": 1, "m_id": "fow-014", "name": "Severance", "img": "\u202aH:\\img\\fow-014.png", "path": "H:\\dongman\\[FOW-014] Severance.mp4"}, {"id": 2, "m_id": "", "name": "\u795e\u66f21", "img": "H:\\img\\\u795e\u66f21.png", "path": "H:\\dongman\\\u795e\u66f21.mkv"}]
# args = {"validate": {"eq": {"body[0]['id']": 1,"body[0]['name']": "Severance"},"uneq": {"body[0][0]": 1}}}
# for i in args["validate"]:
#     if i =="eq":
#         for j in args["validate"][i]:
#             print(j)
#             print(args["validate"][i][j])
#             assert eval(j) == args["validate"][i][j]
import json

body = r'[{"id": 1, "m_id": "fow-014", "name": "Severance", "img": "\u202aH:\\img\\fow-014.png", "path": "H:\\dongman\\[FOW-014] Severance.mp4"}, {"id": 2, "m_id": "", "name": "\u795e\u66f21", "img": "H:\\img\\\u795e\u66f21.png", "path": "H:\\dongman\\\u795e\u66f21.mkv"}]'
body = json.loads(body)

print(body[0])