from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

# template = """
#Você está ensinando uma {pessoa}.
#Explique de modo que a pessoa possa entender.
#"""
#prompt_template = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

messages = [
    SystemMessage('Você é o presidente do {pais}.'),
    MessagesPlaceholder(variable_name="history"),
    HumanMessage('{input}')
]
prompt_template = ChatPromptTemplate.from_messages(messages)
chain = prompt_template | llm | StrOutputParser 

user_input = input("\n> ")
print(prompt_template.invoke({"pais": "Brasil", 'input': user_input}))