import requests
import json
import sys
import csv

url = "http://localhost:11434/api/generate"
prompt = input("\nYou: ").strip()

def call_model(model_name, prompt_text, timeout_seconds=30):
    payload = {
        "model": model_name,
        "prompt": prompt_text,
        "stream": False,
    }
    try:
        resp = requests.post(url, json=payload, timeout=timeout_seconds)
        resp.raise_for_status()
        # Expecting JSON with key 'response'
        return resp.json().get('response', 'No response received')
    except Exception as e:
        return f"ERROR: {e}"

result_llama2 = call_model("llama2", prompt, timeout_seconds=30)
print("\nllama2:", result_llama2)

# Use a longer timeout for Mistral in case the model takes longer to respond
result_mistral = call_model("mistral", prompt, timeout_seconds=120)
print("\nMistral:", result_mistral)

# Write both outputs to a CSV file with header row: llama2,mistral
out_csv = "model_outputs.csv"
try:
    with open(out_csv, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["llama2", "mistral"])
        writer.writerow([result_llama2, result_mistral])
    print(f"\nWrote outputs to {out_csv}")
except Exception as e:
    print(f"Failed to write CSV: {e}")