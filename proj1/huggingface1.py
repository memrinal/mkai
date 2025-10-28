from transformers import AutoTokenizer, AutoModelForCausalLM, TextGenerationPipeline
import torch

def load_local_model(model_name="mistralai/Mistral-7B-Instruct-v0.1"):
    """
    Loads a local Hugging Face model for text generation.
    Replace model_name with your local path or Hugging Face model ID.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    pipe = TextGenerationPipeline(model=model, tokenizer=tokenizer)
    return pipe

def main():
    print("🤖 Welcome to your local Hugging Face Chat Agent!")
    print("Type any prompt you'd like me to respond to. Type 'exit' to quit.\n")

    pipe = load_local_model()

    while True:
        user_prompt = input("📝 Your prompt: ").strip()
        if user_prompt.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        if not user_prompt:
            print("⚠️ Please enter a prompt.")
            continue

        try:
            response = pipe(user_prompt, max_new_tokens=256, temperature=0.7, do_sample=True)
            print("🤖 Assistant:", response[0]["generated_text"].strip())
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()