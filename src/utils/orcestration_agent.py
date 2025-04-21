from langchain_core.tools import Tool
from rag_agent import LLM_with_RAG
from websearch_agent import web_agent
from calculator import calculator
from weather_agent import weather_agent
from prompts import prompt
from dotenv import load_dotenv
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain.agents import create_tool_calling_agent,AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
def orcestartion_agent(query : str):
        
    RAG_AGENT_TOOL = Tool(
        name = "RAG AGENT",
        func = LLM_with_RAG,
        description = "This agent will give answers regarding the oscars"
    )

    WEBSEARCH_AGENT_TOOL = Tool(
        name = "WEB SEARCH AGENT",
        func = web_agent,
        description = "This agent will take a URL and give summary of the information from the given url"
    )

    CALCULATOR_AGENT_TOOL = Tool(
        name = "CALCULATOR AGENT",
        func = calculator,
        description = "This agent will do the addition task for a given 2 number."
    )

    WEATHER_AGENT = Tool(
    name = "WEATHER AGENT",
    func = weather_agent,
    description = "This agent will give the current weather for the given city." 
    )
    tools = [RAG_AGENT_TOOL,WEBSEARCH_AGENT_TOOL,CALCULATOR_AGENT_TOOL,WEATHER_AGENT]

 
    groq_api = os.getenv('GROQ_API_KEY')
    llm= ChatGroq(temperature=0, groq_api_key=groq_api, model_name="llama-3.3-70b-versatile")
    prompt_template = ChatPromptTemplate.from_messages([
        ("system",prompt.orcestration_prompt()),('human',"{input}"),('placeholder','{agent_scratchpad}')
    ])
    agent = create_tool_calling_agent(llm,tools,prompt_template)
    my_agent = AgentExecutor(agent = agent , tools =tools )
    result = my_agent.invoke({'input':query})
    return result


print(orcestartion_agent("best motion film award was won by which movie?"))
print(orcestartion_agent("give me an overview od data in the webpage https://docs.tavily.com/documentation/quickstart"))
#print(orcestartion_agent("what is the sum of {\"a"\:5, \"b"\:2}?))
print(orcestartion_agent("how is the weather in Sacramento?"))