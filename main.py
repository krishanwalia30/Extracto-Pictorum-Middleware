from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests 
import json

class ModelInput(BaseModel):
    image_url: str = ""
    index: int = 0

backend_url = "http://extractopictorumapimodeldeploy.centralindia.azurecontainer.io"

app = FastAPI()
app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["*"],
   allow_headers=["*"],
)

@app.post('/request-detection-of-objects')
def request_detection_of_objects(input_parameters: ModelInput):
    url = backend_url+"/detected-objects-from-url"

    payload = json.dumps({
    "image_url": str(input_parameters.image_url),
    "index": input_parameters.index,
    })

    # payload = json.dumps({
    # "image_url": "https://images.unsplash.com/photo-1719437492355-9686ac0bb4d9?q=80&w=1909&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    # "index": 0
    # })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return response.json()

@app.post('/request-extraction-of-object')
def request_extraction_of_object(input_parameters: ModelInput):
    url = backend_url+"/extracted-object-from-image-url"

    payload = json.dumps({
    "image_url": str(input_parameters.image_url),
    "index": input_parameters.index,
    })

    # payload = json.dumps({
    # "image_url": "https://images.unsplash.com/photo-1719437492355-9686ac0bb4d9?q=80&w=1909&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    # "index": 0
    # })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    return response.json()