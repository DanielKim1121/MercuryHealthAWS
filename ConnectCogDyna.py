import requests
import json

credential = {
  "username": "sadf",
  "password": "sdfasdfasfasdf"
}

r = requests.put("https://asdfasf", json.dumps(credential))

if r.status_code >= 200 and r.status_code < 400:
    print("GOOD")
else:
    print("BAD")

if json.loads(r.content)['id_token'] is not None:
    id_token = json.loads(r.content)['id_token']
    data = {
        "httpMethod":"POST",
        "Username": "werf",
        "Message": "fdafsasdfasdf"
    }
    d = requests.post("https://asdfasdf", json.dumps(data), headers = {"Authorization": id_token})

    if d.status_code >= 200 and d.status_code < 400:
        print("GOOD")
    else:
        print("BAD")
    print(d.content)
