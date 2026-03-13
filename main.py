from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv() # load env variables from .env file

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent = Agent(
    name="Finance Agent",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["You are a finance trading expert, use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent= Agent(
    team=[web_agent, finance_agent],
    model=Gemini(id="gemini-2.5-flash"),
    instructions=["You are a agent router that decides the best agent to respond or call both agents depending on user input/prompt"],
    show_tool_calls=True,
    markdown=True
)


multi_ai_agent.print_response("Analyze latest new and stock prices for NVIDIA", stream=True)
