import requests
import time

today = time.strftime("%Y-%m-%d", time.gmtime())


print(today)

url = "https://httpbin.org/get"
paramsObject = {'q' : today}
headersObject = {'Accept':'application/json'}


response = requests.get(url, params=paramsObject, headers=headersObject)

if response:
    print('Success!')
else:
    print('Failure!')

print(response.json())


