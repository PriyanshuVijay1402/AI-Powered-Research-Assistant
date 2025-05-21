from crewai import Agent
from dotenv import load_dotenv
import os
from langchain_litellm import ChatLiteLLM

# Load environment variables
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if openrouter_api_key is None:
    raise ValueError("OPENROUTER_API_KEY not set in .env")

llm = ChatLiteLLM(
    model="openrouter/mistralai/mistral-7b-instruct",
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Agent 1: Understands the user's query
query_agent = Agent(
    role="Research Query Interpreter",
    goal="Refine the user's research topic into clear keywords",
    backstory="You are skilled at understanding vague research ideas and turning them into precise search queries.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

# Agent 2: Searches arXiv or similar APIs
search_agent = Agent(
    role='Research Paper Retriever',
    goal='Search arXiv and fetch top relevant research papers',
    backstory='Highly skilled in academic search and filtering results',
    verbose=True,
    allow_delegation=True,
    llm=llm,
)

# Agent 3: Summarizes research papers
summarizer_agent = Agent(
    role="Research Paper Summarizer",
    goal="Summarize key findings and contributions of each research paper found concisely.",
    backstory="Expert in academic summarization and NLP with years of research experience.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
)

# Agent 4: Formats and organizes the final output
formatter_agent = Agent(
    role='Research Report Formatter',
    goal='Organize results into a clean, human-readable report',
    backstory='Skilled in creating structured and accessible summaries',
    verbose=True,
    allow_delegation=True,
    llm=llm,
)
