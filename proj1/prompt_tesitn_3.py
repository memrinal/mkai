from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Initialize the LLM
llm = Ollama(model="mistral")

# Create chat prompt template with history support
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that maintains context from previous messages."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{question}")
])

# Create the chain
chain = chat_prompt | llm | StrOutputParser()

# Define conversation history
history = [
    HumanMessage(content="Hi!"),
    AIMessage(content="Hello! How can I help?"),
    HumanMessage(content="I'd like to learn about capitals."),
    AIMessage(content="I'd be happy to help you learn about capital cities! What would you like to know?")
]

# Test the conversation
print("=== Testing Conversation with History ===")
print("\nHistory:")
for msg in history:
    print(f"{'User' if isinstance(msg, HumanMessage) else 'Assistant'}: {msg.content}")

print("\nNew Question:")
response = chain.invoke({
    "history": history,
    "question": "What's the capital of France?"
})
print("\nResponse:")
print(response)
