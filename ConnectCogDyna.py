import requests
import json

credential = {
  "username": "sadf",
  "password": "sdfasdfasfasdf"
}

r = requests.put("https://dto7rhvoe5.execute-api.us-west-2.amazonaws.com/prod/authenticate", json.dumps(credential))

if r.status_code >= 200 and r.status_code < 400:
    print("GOOD")
else:
    print("BAD")

if json.loads(r.content)['id_token'] is not None:
    id_token = json.loads(r.content)['id_token']
    data = {
        "httpMethod":"POST",
        "Username": "asdfaf",
        "Message": "werqwadsfa"
    }
    d = requests.post("https://kayxrpz2ef.execute-api.us-west-2.amazonaws.com/production/data", json.dumps(data), headers = {"Authorization": id_token})

    if d.status_code >= 200 and d.status_code < 400:
        print("GOOD")
    else:
        print("BAD")
    print(d.content)
