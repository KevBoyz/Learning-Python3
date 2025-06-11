from langchain_community.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate
import assemblyai as aai
import os

from dotenv import load_dotenv
load_dotenv()
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

config = aai.TranscriptionConfig(
    language_detection=True,
    filter_profanity=False,
)

audio = 'Data_Science/Langchain_Family/assets/carlinhos.mp3'

loader = AssemblyAIAudioTranscriptLoader(audio, config=config)
docs = loader.load()
# print('\n',docs[0].page_content)

llm = OpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_messages([
    ('system', 'Use isso como contexto: {document}'),
    ('human', 'Do que se trata?')
])

chain = prompt | llm
answer = chain.invoke({'document':docs})

print(f'\n{answer}\n')
