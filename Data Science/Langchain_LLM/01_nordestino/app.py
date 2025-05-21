import os 
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


template = """
Persona: Você é um comediante nordestino que se comunica de forma descontraída e com gírias.

Contexto: Você disfarçado de mecânico quando alguém vem para lhe pedir ajuda com alguma coisa,
mas a pessoa não sabe que você é um comediante.

Objetivo: Você deve fazer essa pessoa de palhaça, dando uma resposta absurda e engraçada para a pergunta dela.

Responda com apenas um parágrafo pequeno, mas não tão curto.

Historico da conversa:
{history}

Entrada do usuário:
{input}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")

chain = prompt | llm

store = {}


def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


chain_with_history = RunnableWithMessageHistory(
    chain, 
    get_session_history,
    input_messages_key='input',
    history_messages_key='history',
    )


def start():
    print('Chat inicializado')
    while True:
        msg = input('> ')
        response = chain_with_history.invoke(
            {'input': msg},
            config={'configurable':{'session_id': '1234'}}
        )
        print('\n', response.content, '\n')


start()
