from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template=ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "Explain the concept of {topic} ")
])


prompt=chat_template.invoke({"domain":"math","topic":"Fourier Transform"})
print(prompt)   
