import requests
import json
import sys

url = "http://localhost:11434/api/generate"
prompt = input("\nYou: ").strip()    
    # Prepare the request payload
data = {
    "model": "mistral",
    "prompt": prompt,
    "stream": False  # Get complete response rather than streaming
    }

response = requests.post(url, json=data)
        
result = response.json().get('response', 'No response received')
        
print("\nMistral:", result)