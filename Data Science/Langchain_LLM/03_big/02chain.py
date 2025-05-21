from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

messages = [  # Usar os objetos de abstração gera promblemas com as labels de human
    ('system', 'Você é o presidente do {pais}'),
    ('human', '{input}')
]
prompt_template = ChatPromptTemplate.from_messages(messages)

format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: llm.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

response = chain.invoke({'pais': 'Brasil', 'input': 'Quantos estados o país tem'})
print(response)