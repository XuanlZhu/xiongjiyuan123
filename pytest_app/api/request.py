import requests
import json

def request(args):
    if args["request"]["method"] == "get":
        r = requests.get(url=args["request"]["url"],headers=args["request"]["headers"],params=args["request"]["params"])
        print(r.text)
        print(r.status_code)
        # assert r.status_code == 200
        body = json.loads(r.text)
        for i in args["validate"]:
            if i == "eq":
                for j in args["validate"][i]:
                    assert eval(j) == args["validate"][i][j]