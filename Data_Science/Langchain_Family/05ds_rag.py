from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from langchain_community.vectorstores import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DataFrameLoader
from datasets import load_dataset
from dotenv import load_dotenv

load_dotenv('.env')



def load_dataset_docs():
    ds = load_dataset('json', data_files='./assets/ministral7b.jsonl')
    df = ds['train'].to_pandas()
    docs = df[['chunk', 'source']]
    loader = DataFrameLoader(docs, page_content_column='chunk')
    return loader.load()


def gen_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    qdrant = Qdrant.from_documents(
        documents,
        embedding=embeddings,
        location=':memory:',
        collection_name='ministral7b'
    )
    return qdrant.as_retriever(search_kwargs={"k": 3})


prompt = ChatPromptTemplate.from_template("""
Responda a pergunta com base no contexto fornecido:

{context}

Entrada do usuário:
{question}
""")


llm = OpenAI(model="gpt-4o-mini")


documents = load_dataset_docs()
retriever = gen_vectorstore(documents)

rag_chain = (   # retriever.invoke debaixo dos panos
    {"context": retriever, "question": RunnableLambda(lambda x: x)}
    | prompt
    | llm
)

while True:
    query = input("Pergunta: ")
    response = rag_chain.invoke(query)

    if response.startswith("Assistant<|im_sep|>"):  # Artefato de formatação do modelo
        response = response.replace("Assistant<|im_sep|>", "", 1).lstrip()

    print(response)
