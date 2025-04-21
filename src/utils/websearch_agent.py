from langchain_community.document_loaders import WebBaseLoader
from prompts import prompt
from langchain_core.tools import tool
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
def web_agent(url : str):
    '''
    web search agent scrapes and get the web page and summarize the data

    Parameters:
    url (str): it is a valid url for a web page

    Returns:
    str: The summarized information for the given url.
    '''
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs[0].page_content

@tool(description="Fetch a webpage and return a 3–5 bullet summary of its main content")
def web_agent_summary(url : str):
    web_context = web_agent(url)
    the_prompt=prompt()
    my_prompt=the_prompt.web_prompt()
    new_prompt = my_prompt.format(context=web_context)

    groq_api = os.getenv('GROQ_API_KEY')

    client = Groq(
        api_key=groq_api
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

#web_agent_summary("https://docs.tavily.com/documentation/quickstart")