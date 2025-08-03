from crewai import Agent
from tools.citation_tool import fetch_citations

citation_agent = Agent(
    role="Citation Agent",
    goal="Enhance simplified research text with appropriate citations or source references.",
    backstory="You are a research librarian and scientific analyst who enriches summaries with authoritative references using trusted academic databases.",
    tools=[fetch_citations],
    verbose=True
)
