import os
import logging
from swarm import Swarm, Agent

# Set up logging
logging.basicConfig(
    filename='agent_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ensure the API key is set correctly in the environment
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment variables")

client = Swarm()  # No 'api_key' argument, Swarm reads from environment

# Define Agent 1: Market Trends Analyst
agent1 = Agent(
    name="MarketTrendsAnalyst",
    instructions="Analyze current market trends in the US automobile industry, focusing on consumer preferences, emerging technologies, and competitor offerings."
)

# Define Agent 2: Product Development Consultant
agent2 = Agent(
    name="ProductDevelopmentConsultant",
    instructions="Based on market trends, recommend features, specifications, and design elements for a new car model that will appeal to US consumers."
)

# Define Agent 3: Launch Strategy Advisor
agent3 = Agent(
    name="LaunchStrategyAdvisor",
    instructions="Develop a launch strategy for the new car model, considering the recommended features and current market conditions."
)

# Prepare messages for Agent 1
messages1 = [
    {"role": "user", "content": "As the CEO, I need an analysis of the current US automobile market trends to inform our new car model development."}
]

# Run the agents with inter-agent communication
try:
    # Run Agent 1: Market Trends Analyst
    response1 = client.run(agent=agent1, messages=messages1)
    print("Market Trends Analyst Response:")
    print(response1)
    # Log the response
    logging.info(f"Agent 1 Response: {response1}")

    # Prepare messages for Agent 2, including output from Agent 1
    messages2 = [
        {"role": "user", "content": f"Based on the market trends analysis: {response1}, what features and specifications should our new car model have to succeed in the US market?"}
    ]

    # Run Agent 2: Product Development Consultant
    response2 = client.run(agent=agent2, messages=messages2)
    print("\nProduct Development Consultant Response:")
    print(response2)
    # Log the response
    logging.info(f"Agent 2 Response: {response2}")

    # Prepare messages for Agent 3, including output from Agent 2
    messages3 = [
        {"role": "user", "content": f"Given the recommended features and specifications: {response2}, develop a marketing and launch strategy for the US market."}
    ]

    # Run Agent 3: Launch Strategy Advisor
    response3 = client.run(agent=agent3, messages=messages3)
    print("\nLaunch Strategy Advisor Response:")
    print(response3)
    # Log the response
    logging.info(f"Agent 3 Response: {response3}")

except Exception as e:
    print(f"An error occurred: {e}")
    logging.error(f"An error occurred: {e}")
