#from utils.embeddings import sentence_transformer_embeding_model
from embeddings import sentence_transformer_embeding_model
from langchain_chroma import Chroma
from groq import Groq
from dotenv import load_dotenv
import os
from prompts import prompt
from langchain_core.tools import tool

# Load environment variables from .env file
load_dotenv()

def format_text(docs : list):
    text = ""
    for d in docs:
        text += d.page_content+'\n'
    return text
# format_text([(page_content:'test'),{'page_content':'new test'}])

def similarity_search(query : str, k : int = 10):
    my_embed_model = sentence_transformer_embeding_model()
    per_dir='./newchromadb_file'
    collection_name='oscars'
    db = Chroma(
        collection_name=collection_name,
        persist_directory=per_dir,
        embedding_function=my_embed_model)
    
    docs = db.similarity_search(query,k = k)

    return format_text(docs)

#print(similarity_search("how many awards did Poor Things won"))
@tool
def LLM_with_RAG(query):
    '''
    this is a rag function that will give answers regarding the oscars

    parameters: 
    question (str) : a question grom the user

    return:
    str : a valid answer to the question

    '''
    context = similarity_search(query)
    my_prompt = prompt.rag_prompt()
    new_prompt = my_prompt.format(context=context,question=query)
    
    groq_api_key=os.getenv('GROQ_API_KEY')
    client = Groq(
        api_key=groq_api_key
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": new_prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

#LLM_with_RAG("who is best supporting actress")