import os
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool
from dotenv import load_dotenv

# Load your API key
load_dotenv()

# Set up to use Groq
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama-3.3-70b-versatile"

# Create scraping tool - no API key needed!
scrape_tool = ScrapeWebsiteTool()

# Create news reporter agent
newsreporter = Agent(
    role='News Reporter',
    goal='Scrape news websites and extract the latest headlines',
    backstory='You are a tech-savvy journalist who can read news websites and extract important information.',
    verbose=True,
    allow_delegation=False,
    tools=[scrape_tool]
)

# Create task - tell agent which sites to scrape
newsreporter_task = Task(
    description='''
    Scrape these news websites and give me the top 5 headlines:
    - https://www.bbc.com/news
    - https://news.ycombinator.com
    
    Extract the main headlines from these sites.
    ''',
    agent=newsreporter,
    expected_output='A list of 5 top headlines from BBC News and Hacker News'
)

# Create crew
crew = Crew(
    agents=[newsreporter],
    tasks=[newsreporter_task],
    verbose=True
)

# Run!
print("\n🚀 Starting news agent with web scraping...\n")
result = crew.kickoff()

print("\n" + "="*50)
print("✅ NEWS HEADLINES:")
print("="*50)
print(result)
print("="*50 + "\n")
