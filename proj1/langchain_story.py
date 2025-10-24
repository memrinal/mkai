from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def create_conversation_chain():
    # Initialize Ollama with Mistral model
    llm = Ollama(model="mistral", temperature=0.7)
    
    # Create a prompt template that maintains context
    prompt = PromptTemplate.from_template(
        """You are a helpful and knowledgeable assistant. 
Please provide a clear and informative response to the following question:

Question: {question}

Answer: """
    )
    
    # Create a chain using the new LangChain expression syntax
    chain = prompt | llm | StrOutputParser()
    return chain

def main():
    # Create the conversation chain
    conversation = create_conversation_chain()
    
    print("Welcome! I'm your AI assistant powered by Mistral.")
    print("You can ask me questions, and I'll do my best to help.")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        # Get user input
        user_input = input("\nYour question: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit']:
            print("\nGoodbye! Have a great day!")
            break
        
        if not user_input:
            print("Please ask a question!")
            continue
        
        try:
            # Get response from the chain
            response = conversation.invoke({"question": user_input})
            print("\nAssistant:", response.strip())
        except Exception as e:
            print(f"\nError: Something went wrong - {str(e)}")
            print("Please try again with a different question.")

if __name__ == "__main__":
    main()
