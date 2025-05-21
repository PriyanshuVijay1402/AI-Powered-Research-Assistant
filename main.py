from crewai import Crew, Task
from agents import query_agent, search_agent, summarizer_agent, formatter_agent

# Task 1: Interpret the user's query
query_task = Task(
    description="Analyze the user's topic: '{{user_input}}'. Extract and return 2–10 keywords suitable for searching research papers on arXiv.",
    expected_output="A refined search query (keywords or a short descriptive phrase).",
    agent=query_agent
)

# Task 2: Search arXiv
search_task = Task(
    description="Using the refined query from Task 1, search arXiv and retrieve metadata of the top 3–5 relevant papers (title, authors, abstract, link).",
    expected_output="A list of papers with title, authors, abstract, and arXiv link.",
    agent=search_agent,
    context=[query_task]
)

summarize_task = Task(
    description="Summarize the abstracts of the selected papers clearly and concisely. Focus on the topic of '{{user_input}}'.",
    expected_output="Summarized abstracts of each paper, suitable for a non-expert reader.",
    agent=summarizer_agent,
    context=[search_task]
)

format_task = Task(
    description="Create a clean, structured summary report with all relevant information. Ensure that the report is related only to '{{user_input}}'.",
    expected_output="Formatted research report with headings, summaries, and links.",
    agent=formatter_agent,
    context=[summarize_task]
)


# Create the crew
crew = Crew(
    agents=[query_agent, search_agent, summarizer_agent, formatter_agent],
    tasks=[query_task, search_task, summarize_task, format_task],
    verbose=True
)

# Run the crew
user_input = input("Enter your research topic: ")
result = crew.kickoff(inputs={"user_input": user_input})
print("\n\n📝 Final Research Report:\n")
print(result)