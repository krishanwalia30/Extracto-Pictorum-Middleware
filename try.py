import requests
import json

url = "http://extractopictorumapimodeldeploy.centralindia.azurecontainer.io/detected-objects-from-url"

payload = json.dumps({
  "image_url": "https://images.unsplash.com/photo-1719437492355-9686ac0bb4d9?q=80&w=1909&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  "index": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
