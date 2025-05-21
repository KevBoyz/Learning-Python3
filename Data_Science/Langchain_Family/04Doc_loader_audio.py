from langchain_community.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI


from dotenv import load_dotenv
load_dotenv()

audio = 'Data_Science/Langchain_Family/assets/audio.ogg'

loader = AssemblyAIAudioTranscriptLoader(audio)
docs = loader.load()
# print('\n',docs[0].page_content)

llm = OpenAI(model="gpt-4o-mini")
qa_chain = load_qa_chain(llm, chain_type='stuff')

answer = qa_chain.invoke(input={'input_documents': docs,
                                'question': 'What this is about?'})

print('\n', answer['output_text'])
