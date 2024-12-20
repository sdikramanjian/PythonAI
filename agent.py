# This class ia an example of an Agent built with Langchain

# Import relevant functionality
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
import getpass
import os
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

class Agent:
#define the class level variables 
    memory = None
    model = None
    search  = None
    tools = None
    agent_executor = None
    model_name="claude-3-sonnet-20240229"
    max_results=5
    tavility_api_key = "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"

    def __init__(self):
       if not os.environ.get("TAVILY_API_KEY"):
         os.environ["TAVILY_API_KEY"] = self.tavility_api_key
       self.memory = MemorySaver()
       self. model = ChatAnthropic(model_name=self.model_name)
       self.search = TavilySearchResults(max_results = self.max_results)
       self.tools = [self.search]
       self.agent_executor = create_react_agent(self.model, self.tools, checkpointer=self.memory)
      
    def GetData(self):
       print(self.tools[0].invoke("WHo won the french open"))
        # config = {"configurable": {"thread_id": "abc123"}}
        # for chunk in self.agent_executor.stream(
        #     {"messages": [HumanMessage(content="Who won the last french open")]} , config
        # ):
        #     print(chunk)
        #     print("----")

        # for chunk in self.agent_executor.stream(
        #     {"messages": [HumanMessage(content="whats the weather where I live?")]} , config
        # ):
        #     print(chunk)
        #     print("----")