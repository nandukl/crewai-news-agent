print("Program Started")

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# Load .env
load_dotenv()

print("Gemini Key:", os.getenv("GEMINI_API_KEY"))
# Configure Gemini
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Ask the user for a topic
topic = input("Enter a topic to research: ")

# Research Agent
researcher = Agent(
    role="Researcher",
    goal=f"Research the topic: {topic}",
    backstory="You are an experienced AI researcher who finds accurate and useful information.",
    llm=llm,
    verbose=True
)

# Writer Agent
writer = Agent(
    role="Writer",
    goal="Write a clear and engaging report.",
    backstory="You are a professional technical writer.",
    llm=llm,
    verbose=True
)

# Research Task
research_task = Task(
    description=f"Research the topic '{topic}' and collect the important information.",
    expected_output="Detailed research notes.",
    agent=researcher
)

# Writing Task
writing_task = Task(
    description="Write a well-structured report based on the research.",
    expected_output="A final report in simple language.",
    agent=writer,
    context=[research_task]  # Pass researcher's output to the writer
)

# Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# Execute
result = crew.kickoff()

# Display
print("\n========== FINAL REPORT ==========\n")
print(result)

# Save the report (always saved next to this script)
report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.txt")
with open(report_path, "w", encoding="utf-8") as file:
    file.write(str(result))

print("\nReport saved as", report_path)