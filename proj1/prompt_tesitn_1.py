from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


llm = Ollama(model="mistral")

prompt = PromptTemplate.from_template("Translate the following to French:\n{text}")
chain = prompt | llm | StrOutputParser()

response = chain.invoke({"text": "Good morning"})
print(response)