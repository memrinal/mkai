import requests
import json
import sys

url = "http://localhost:11434/api/generate"

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


def process_questions(questions_file="questions.txt", answers_file="answers.txt"):
    try:
        with open(questions_file, "r", encoding="utf-8") as qf:
            questions = [line.rstrip('\n') for line in qf]
    except FileNotFoundError:
        print(f"Questions file '{questions_file}' not found. Create it with one question per line.")
        return

    try:
        with open(answers_file, "w", encoding="utf-8") as outf:
            for idx, raw in enumerate(questions, start=1):
                question = raw.strip()
                if not question:
                    continue

                outf.write(f"Question {idx}: {question}\n")

                # Call Llama2 (shorter timeout)
                llama_resp = call_model("llama2", question, timeout_seconds=30)
                outf.write("llama2: \n")
                outf.write(llama_resp + "\n\n")

                # Call Mistral (longer timeout)
                mistral_resp = call_model("mistral", question, timeout_seconds=120)
                outf.write("Mistral: \n")
                outf.write(mistral_resp + "\n")

                outf.write("\n---\n\n")

        print(f"Wrote answers to {answers_file}")
    except Exception as e:
        print(f"Failed to write answers: {e}")


if __name__ == "__main__":
    # Allow optional custom filenames via command-line args
    qfile = sys.argv[1] if len(sys.argv) > 1 else "questions.txt"
    afile = sys.argv[2] if len(sys.argv) > 2 else "answers.txt"
    process_questions(qfile, afile)