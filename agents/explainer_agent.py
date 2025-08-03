from crewai import Agent
from tools.simplify_text_tool import simplify_text

explainer_agent = Agent(
    role="Explainer Agent",
    goal="Convert complex research paper sections into simplified explanations that are understandable to undergraduates.",
    backstory="You are a science communicator and educator who breaks down complex concepts into easy-to-grasp summaries using clear and engaging language.",
    tools=[simplify_text],
    verbose=True
)