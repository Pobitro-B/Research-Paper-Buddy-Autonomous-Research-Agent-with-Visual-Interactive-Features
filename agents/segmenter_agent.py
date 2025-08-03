from crewai import Agent
from tools.segment_text_tool import segment_text

segmenter_agent = Agent(
    role="Segmenter Agent",
    goal="Divide long sections of research text into coherent, manageable chunks for downstream processing.",
    backstory="You are a preprocessing expert who understands how to chunk scientific documents semantically for optimal comprehension and analysis.",
    tools=[segment_text],
    verbose=True
)