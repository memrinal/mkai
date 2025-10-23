import requests
import json
import sys

url = "http://localhost:11434/api/generate"
prompt = input("\nYou: ").strip()    
    # Prepare the request payload
data_ollama_llama2 = {
    "model": "llama2",
    "prompt": prompt,
    "stream": False  # Get complete response rather than streaming
    }

response = requests.post(url, json= data_ollama_llama2)
        
result = response.json().get('response', 'No response received')
        
print("\nllama2:", result)

data_ollama_mistral = {
    "model": "mistral",
    "prompt": prompt,
    "stream": False  # Get complete response rather than streaming
    }

response = requests.post(url, json=data_ollama_mistral)
        
result = response.json().get('response', 'No response received')
        
print("\nMistral:", result)