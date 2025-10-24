import re

def get_weather(city: str) -> str:
    """Get Weather for a Given City (dummy implementation)."""
    return f"The weather in {city} is sunny with a high of 25°C."

def create_agent(model, tools, system_prompt):
    """Create a minimal local agent that calls the provided tools.

    This is a lightweight replacement for environments where external
    packages (like langchain) are not available.
    """
    class Agent:
        def __init__(self, model, tools, system_prompt):
            self.model = model
            self.tools = tools
            self.system_prompt = system_prompt

        def invoke(self, payload):
            messages = payload.get("messages", [])
            if not messages:
                return {"error": "no messages provided"}
            content = messages[-1].get("content", "")
            # Try to extract the city after the word 'in'
            m = re.search(r"in\s+([A-Za-z0-9 ._-]+)$", content.strip(), re.IGNORECASE)
            if m:
                city = m.group(1).strip()
            else:
                # fallback: take last token
                city = content.strip().split()[-1]
            try:
                result = self.tools[0](city)
                return {"response": result}
            except Exception as e:
                return {"error": str(e)}

    return Agent(model, tools, system_prompt)


if __name__ == "__main__":
    agent = create_agent(
        model="mistral",
        tools=[get_weather],
        system_prompt="You are a meteorological assistant that provides weather information based on user queries.",
    )

    result = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
    if 'response' in result:
        print(result['response'])
    else:
        print('Error:', result.get('error'))