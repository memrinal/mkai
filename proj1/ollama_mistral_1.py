import requests
import json
import sys

def query_mistral(prompt):
    """
    Send a prompt to locally running Ollama Mistral model and get the response
    """
    url = "http://localhost:11434/api/generate"
    
    # Prepare the request payload
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False  # Get complete response rather than streaming
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise exception for bad status codes
        
        result = response.json()
        return result.get('response', 'No response received')
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure Ollama is running and Mistral model is installed.")
        print("To install Mistral model: ollama pull mistral")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while communicating with Ollama: {e}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Received invalid response from Ollama")
        sys.exit(1)

def main():
    print("Ollama Mistral Chat (Press Ctrl+C to exit)")
    print("----------------------------------------")
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            # Get response from Mistral
            response = query_mistral(user_input)
            
            # Print the response
            print("\nMistral:", response)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()