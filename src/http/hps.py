import requests

url = 'http://localhost:8080/hps/message/maintainMessage/getAlarmDetail'

params = {
    'id': 1009
}

j = 0
while j < 1000:
    result = requests.post(url, json=params, headers={'Content-Type': 'application/json;charset=UTF-8'})
    print result.content
    j += 1
