from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def test_system_prompt(system_prompt: str, user_query: str, topic: str):
    """Test how different system prompts affect the response."""
    llm = Ollama(model="mistral")
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_query)
    ])
    
    chain = chat_prompt | llm | StrOutputParser()
    
    print(f"\n=== Testing System Prompt ===")
    print(f"System: {system_prompt}")
    print(f"User Query: {user_query.format(topic=topic)}")
    print(f"Response:\n")
    response = chain.invoke({"topic": topic})
    print(response)
    print("=" * 50)

# Test different system prompts
prompts_to_test = [
    "You are a professional volleyball player who is very active and wants to make everyone active.",
    "You are a businessman who thinks of money and investments all the time.",
    "You are a software engineer who is trying to learn LLM",
    "You are a zen master who speaks in riddles and metaphors",
    "You are a cat behaviorist who understands feline psychology"
]

# Test each prompt with the same user query
for prompt in prompts_to_test:
    test_system_prompt(
        system_prompt=prompt,
        user_query="Tell me a joke about {topic}",
        topic="cats"
    )
    # Add a small pause between requests
    import time
    time.sleep(1)
