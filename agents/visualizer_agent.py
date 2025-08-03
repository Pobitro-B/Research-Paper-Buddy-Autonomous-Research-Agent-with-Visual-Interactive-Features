from crewai import Agent
from tools.visualizer_tool import generate_visuals

visualizer_agent = Agent(
    role="Visualizer Agent",
    goal="Create clear and concise diagrams from procedural or methodological descriptions in research papers.",
    backstory="You are a visual design assistant skilled in converting structured processes into flowcharts and method diagrams to improve understanding.",
    tools=[generate_visuals],
    verbose=True
)