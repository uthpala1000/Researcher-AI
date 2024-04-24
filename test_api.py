import requests
import json

import requests

url = "http://127.0.0.1:8000/research"
data = {
    "query": "Metas latest products and news"
}

response = requests.post(url, json=data)
print(response.json())
