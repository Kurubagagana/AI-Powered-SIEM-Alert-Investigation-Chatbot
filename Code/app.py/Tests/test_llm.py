import requests
import time

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3",
    "prompt": "Say Hello",
    "stream": False
}

start = time.time()

response = requests.post(url, json=payload, timeout=180)

print("Status:", response.status_code)
print("Time:", round(time.time() - start, 2), "seconds")
print(response.json()["response"])