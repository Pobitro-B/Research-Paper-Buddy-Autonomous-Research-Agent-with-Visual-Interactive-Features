from crewai import Agent
from tools.parse_pdf_tool import ParsePDFTool

reader_agent = Agent(
    role="Reader Agent",
    goal="Extract structured sections and metadata from uploaded research paper PDFs.",
    backstory="You are a scholarly assistant trained to accurately read and decompose scientific papers into clean sections such as Abstract, Methods, and Conclusion.",
    tools=[ParsePDFTool()],
    verbose=True,
    allow_delegation=False
)