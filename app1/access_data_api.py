import requests
import json
def access_data():
    URL="http://127.0.0.1:8000/get/1"
    response=requests.get(URL)
    r=response.json()

    complex_data=json.dumps(r)
    return complex_data
response=access_data()
print(response)
