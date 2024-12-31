
import os 
from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()

# Web Search Agent 

web_search_agent = Agent(
    name = "web search agent",
    role = "search the web for financial information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include the source of the information in your search query."],
    show_tool_calls = True,
    markdown = True,
)


# Financial Agent

financial_agent = Agent(
    name = "financial agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, 
                           stock_fundamentals=True, company_news=True)],
    instructions = ["Use tables to display the information."],
    show_tool_calls = True,
    markdown = True,

)



multi_ai_agent = Agent(
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    team = [web_search_agent, financial_agent],
    instructions = ["Use the web search agent to find information and the financial agent to analyze it."],
    show_tool_calls = True, 
    markdown = True,
)


multi_ai_agent.print_response("Summarize analyst recommendations for SBI.")