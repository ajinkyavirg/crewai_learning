import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()

# Set up to use Groq
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama-3.3-70b-versatile"

# Create your first AI agent
newsreporter = Agent(
    role='Provide news headlines',
    goal='Provide this weeks global news headlines & trending news',
    backstory='You are a great news media expert who keeps track of global news headlines and what is going on in the world.',
    verbose=True,
    allow_delegation=False
)

# Create a task for the agent
newsreporter_task = Task(
    description='Tell me 10 top world news headlines and short descriptions.',
    agent=newsreporter,
    expected_output='Clear list of top 10 global news headlines and short info'
)

# Create a crew (team of agents) with your agent
crew = Crew(
    agents=[newsreporter],
    tasks=[newsreporter_task],
    verbose=True
)

# Run your crew!
print("\n🚀 Starting your first AI agent...\n")
result = crew.kickoff()

print("\n" + "="*50)
print("✅ RESULT FROM YOUR AI AGENT:")
print("="*50)
print(result)
print("="*50 + "\n")
