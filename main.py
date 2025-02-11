# from agents.triage_agent import triage_agent
# from agents.sales_agent import sales_agent
# from agents.company_partner_agent import company_partner_agent

# def test_agents():
#     print("Testing Triage Agent...")
#     print(triage_agent("How can I solve a server issue?"))

#     print("\nTesting Sales Agent...")
#     print(sales_agent("What products do you have for sale?"))

#     print("\nTesting Company and Partner Info Agent...")
#     print(company_partner_agent("What partners work with your company?"))

# if __name__ == "__main__":
#     test_agents()
# ////////////
# from dotenv import load_dotenv
# import os
# from openai import OpenAI
# from agents.triage_agent import triage_agent
# from agents.sales_agent import sales_agent
# from agents.company_partner_agent import company_partner_agent

# # Load the API key from the .env file
# load_dotenv(dotenv_path='/Users/pass1234/vsCode/bigser/configs/.env')  # Ensure the correct path

# api_key = os.getenv("API_KEY")  # Fetch the API key from environment variables

# if not api_key:
#     raise ValueError("API key not found. Make sure it's set in the .env file under 'API_KEY'.")

# # Initialize the OpenAI client with the loaded API key
# client = OpenAI(api_key=api_key)

# def test_agents():
#     print("Testing Triage Agent...")
#     print(triage_agent(client, "How can I solve a server issue?"))

#     print("\nTesting Sales Agent...")
#     print(sales_agent(client, "What products do you have for sale?"))

#     print("\nTesting Company and Partner Info Agent...")
#     print(company_partner_agent(client, "What partners work with your company?"))

# if __name__ == "__main__":
#     test_agents()
# /////////
from dotenv import load_dotenv
import os
from openai import OpenAI
from agents.triage_agent import triage_agent


# Load the API key from the .env file
load_dotenv(dotenv_path='/Users/pass1234/vsCode/bigser/configs/.env')  # Ensure the correct path

api_key = os.getenv("API_KEY")  # Fetch the API key from environment variables

if not api_key:
    raise ValueError("API key not found. Make sure it's set in the .env file under 'API_KEY'.")

# Initialize the OpenAI client with the loaded API key
client = OpenAI(api_key=api_key)

# Function to simulate conversation with the agent
def simulate_conversation_with_agent(agent_function):
    user_input = input("You: ")  # Start the conversation with user input
    while True:
        print(f"Agent: {agent_function(client, user_input)}")  # The agent responds
        user_input = input("You: ")  # User provides the next input

if __name__ == "__main__":
    # Simulate conversation with specific agents
    print("\n--- Starting Conversation with Triage Agent ---")
    simulate_conversation_with_agent(triage_agent)

    print("\n--- Starting Conversation with Sales Agent ---")
    simulate_conversation_with_agent(sales_agent)

    print("\n--- Starting Conversation with Company and Partner Info Agent ---")
    simulate_conversation_with_agent(company_partner_agent)
